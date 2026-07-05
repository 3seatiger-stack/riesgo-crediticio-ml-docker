from pydantic import BaseModel, Field, ConfigDict


class CreditApplication(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "ingreso_mensual": 32000,
                "antiguedad_laboral": 5.5,
                "saldo_promedio": 18000,
                "utilizacion_credito": 0.65,
                "historial_moras": 2,
                "relacion_deuda_ingreso": 0.42,
                "edad_cuenta": 6.0,
                "consultas_buro": 3,
                "variabilidad_ingreso": 0.20,
                "monto_solicitado": 85000
            }
        }
    )

    ingreso_mensual: float = Field(ge=0, le=1_000_000)
    antiguedad_laboral: float = Field(ge=0, le=60)
    saldo_promedio: float = Field(ge=0, le=10_000_000)
    utilizacion_credito: float = Field(ge=0, le=1)
    historial_moras: int = Field(ge=0, le=100)
    relacion_deuda_ingreso: float = Field(ge=0, le=1)
    edad_cuenta: float = Field(ge=0, le=100)
    consultas_buro: int = Field(ge=0, le=100)
    variabilidad_ingreso: float = Field(ge=0, le=1)
    monto_solicitado: float = Field(ge=0, le=100_000_000)


class PredictionResponse(BaseModel):
    prediccion: int
    clasificacion: str
    probabilidad_incumplimiento: float
    umbral_decision: float
    modelo: str
    recomendacion: str
