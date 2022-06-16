from argparse import ArgumentParser
from database.database import LinesDataLoader, DataSheetsEnum
from preprocessing.preprocessing  import LinesDataPreprocesser
from preprocessing.transformation  import LinesFeatureExtractor, FeatureExtractionFields
from models.models import ModelProxy, ModelKind
from evaluation.metrics import MetricsKind, ClassificationMetricsEnum, ClassificationMetricsCalculator
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from collections import Counter
from imblearn.over_sampling import SMOTE

def make_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--n_estimators", type=int)
    parser.add_argument("--max_depth", type=int)
    return parser

if __name__ == "__main__":
    parser = make_parser()
    args = parser.parse_args()
    print(args)

    sheets = { DataSheetsEnum.LINEAS_ACTIVAS : 'Lineas activas hasta 2019',
               DataSheetsEnum.CLIENTES_ACTIVAS: 'Clientes lineas activas',
               DataSheetsEnum.LINEAS_RETIRADAS: 'Lineas retiradas 2017-2019',
               DataSheetsEnum.CLIENTES_RETIRADAS: 'Clientes lineas retir 2017-2019',
               DataSheetsEnum.QUEJAS: 'Quejas lineas',
               DataSheetsEnum.RECLAMOS: 'Reclamos lineas'
            }

    loader = (LinesDataLoader().add_path("/home/hduser/datasets/dataproyecto.xlsx")
                            .load(sheets)
                            .MergeLinesData("codigo del cliente"))

    preprocesser = (LinesDataPreprocesser(loader.get_data(), loader.get_data_claims(), loader.get_data_complaints())
                    .AdjustColumnsNames()
                    .CleanData(['valor_plan'],['saldo_pendiente'])
                    .SetIndex()
                    .AddFeatures()
                    .DropFeatures(['valor_en_reclamo', 'tipo_de_cliente', 'codigo_estado', 'codigo_del_cliente', 'estado',
                                    'fecha_de_instalacion', 'fecha_de_retiro', 'fecha_de_nacimiento'])
                    )
    data = preprocesser.add_data()
    #data.info()
    #data.describe()

    extractor = (
            LinesFeatureExtractor()
            .add_data(data)
            .add_fields(
                FeatureExtractionFields(
                    label = "clase",
                    categorical = ["plan", "tipo_de_plan", "ciclo", "tipo_de_identificacion","estado_financiero", "ciudad"],
                    ordinal = ["edad", "antiguedad"],
                    numeric = ["valor_plan","nro_promedio_quejas_anual","nro_promedio_reclamos_anual","valor_promedio_reclamos_anual","saldo_pendiente"]
                    )
                )
            )

    X, y = extractor.extract() 

    print(X.shape)
    print(y.shape)

    metrics_kind = MetricsKind(accuracy=True, f1_score=True)
    metrics_calculator = ClassificationMetricsCalculator(metrics_kind)

    model_proxy = (
            ModelProxy()
            .add_model_kind(ModelKind.RANDOM_FOREST)
            .add_hparams(n_estimators=args.n_estimators, max_depth=args.max_depth)
            )

    with mlflow.start_run():

        mlflow.log_param("n_estimators", args.n_estimators)
        mlflow.log_param("max_depth", args.max_depth)

        model = model_proxy.resolve()

        print('Original dataset shape %s' % Counter(y))
        sm = SMOTE(random_state=42) 
        X_res, y_res = sm.fit_resample(X, y)
        print('Resampled dataset shape %s' % Counter(y_res))

        X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.3, random_state=1)
        model.fit(X_train,y_train)
        y_pred = model.predict(X_test)
        
        metrics = metrics_calculator.compute(y_test, y_pred)
        print(metrics)

        extractor.save("/home/hduser/datasets/features")

        mlflow.log_artifact("/home/hduser/datasets/features_x.npy")
        mlflow.log_artifact("/home/hduser/datasets/features_y.npy")

        for metric in ClassificationMetricsEnum:
            metric_name = metric.name.lower()
            value = metrics.dict()[metric_name]
            if value is not None:
                mlflow.log_metric(metric_name, value)
        mlflow.sklearn.log_model(model, "project_mlds6_rf")

