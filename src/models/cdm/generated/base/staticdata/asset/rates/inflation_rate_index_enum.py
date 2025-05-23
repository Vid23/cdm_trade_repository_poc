from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class InflationRateIndexEnum(CdmModelBase):
    """The enumerated values to specify the list of inflation rate indices."""
    # Enum values
    AUD_CPI: ClassVar[str] = "AUD-CPI"
    AUS_CPI: ClassVar[str] = "AUS-CPI"
    AUS_HICP: ClassVar[str] = "AUS-HICP"
    BLG_CPI_GI: ClassVar[str] = "BLG-CPI-GI"
    BLG_CPI_HI: ClassVar[str] = "BLG-CPI-HI"
    BLG_HICP: ClassVar[str] = "BLG-HICP"
    BRL_IGPM: ClassVar[str] = "BRL-IGPM"
    BRL_IPCA: ClassVar[str] = "BRL-IPCA"
    CAD_CPI: ClassVar[str] = "CAD-CPI"
    CLP_CPI: ClassVar[str] = "CLP-CPI"
    CNY_CPI: ClassVar[str] = "CNY-CPI"
    CZK_CPI: ClassVar[str] = "CZK-CPI"
    DEK_CPI: ClassVar[str] = "DEK-CPI"
    DEK_HICP: ClassVar[str] = "DEK-HICP"
    DEM_CPI: ClassVar[str] = "DEM-CPI"
    DEM_CPI_NRW: ClassVar[str] = "DEM-CPI-NRW"
    DEM_HICP: ClassVar[str] = "DEM-HICP"
    ESP_CPI: ClassVar[str] = "ESP-CPI"
    ESP_HICP: ClassVar[str] = "ESP-HICP"
    ESP_R_CPI: ClassVar[str] = "ESP-R-CPI"
    ESP_R_HICP: ClassVar[str] = "ESP-R-HICP"
    EUR_AI_CPI: ClassVar[str] = "EUR-AI-CPI"
    EUR_AI_R_CPI: ClassVar[str] = "EUR-AI-R-CPI"
    EUR_EXT_CPI: ClassVar[str] = "EUR-EXT-CPI"
    EUR_EXT_R_CPI: ClassVar[str] = "EUR-EXT-R-CPI"
    FIN_CPI: ClassVar[str] = "FIN-CPI"
    FIN_HICP: ClassVar[str] = "FIN-HICP"
    FRC_EXT_CPI: ClassVar[str] = "FRC-EXT-CPI"
    FRC_HICP: ClassVar[str] = "FRC-HICP"
    GRD_CPI: ClassVar[str] = "GRD-CPI"
    GRD_HICP: ClassVar[str] = "GRD-HICP"
    HKD_CPI: ClassVar[str] = "HKD-CPI"
    HUF_CPI: ClassVar[str] = "HUF-CPI"
    IDR_CPI: ClassVar[str] = "IDR-CPI"
    ILS_CPI: ClassVar[str] = "ILS-CPI"
    IRL_CPI: ClassVar[str] = "IRL-CPI"
    IRL_HICP: ClassVar[str] = "IRL-HICP"
    ISK_CPI: ClassVar[str] = "ISK-CPI"
    ISK_HICP: ClassVar[str] = "ISK-HICP"
    ITL_BC_EXT_CPI: ClassVar[str] = "ITL-BC-EXT-CPI"
    ITL_BC_INT_CPI: ClassVar[str] = "ITL-BC-INT-CPI"
    ITL_HICP: ClassVar[str] = "ITL-HICP"
    ITL_WC_EXT_CPI: ClassVar[str] = "ITL-WC-EXT-CPI"
    ITL_WC_INT_CPI: ClassVar[str] = "ITL-WC-INT-CPI"
    JPY_CPI_EXF: ClassVar[str] = "JPY-CPI-EXF"
    KRW_CPI: ClassVar[str] = "KRW-CPI"
    LUX_CPI: ClassVar[str] = "LUX-CPI"
    LUX_HICP: ClassVar[str] = "LUX-HICP"
    MXN_CPI: ClassVar[str] = "MXN-CPI"
    MXN_UDI: ClassVar[str] = "MXN-UDI"
    MYR_CPI: ClassVar[str] = "MYR-CPI"
    NLG_CPI: ClassVar[str] = "NLG-CPI"
    NLG_HICP: ClassVar[str] = "NLG-HICP"
    NOK_CPI: ClassVar[str] = "NOK-CPI"
    NZD_CPI: ClassVar[str] = "NZD-CPI"
    PER_CPI: ClassVar[str] = "PER-CPI"
    PLN_CPI: ClassVar[str] = "PLN-CPI"
    POR_CPI: ClassVar[str] = "POR-CPI"
    POR_HICP: ClassVar[str] = "POR-HICP"
    RUB_CPI: ClassVar[str] = "RUB-CPI"
    SEK_CPI: ClassVar[str] = "SEK-CPI"
    SGD_CPI: ClassVar[str] = "SGD-CPI"
    SWF_CPI: ClassVar[str] = "SWF-CPI"
    TRY_CPI: ClassVar[str] = "TRY-CPI"
    TWD_CPI: ClassVar[str] = "TWD-CPI"
    UK_CPIH: ClassVar[str] = "UK-CPIH"
    UK_HICP: ClassVar[str] = "UK-HICP"
    UK_RPI: ClassVar[str] = "UK-RPI"
    UK_RPIX: ClassVar[str] = "UK-RPIX"
    USA_CPI_U: ClassVar[str] = "USA-CPI-U"
    ZAR_CPI: ClassVar[str] = "ZAR-CPI"
    ZAR_CPIX: ClassVar[str] = "ZAR-CPIX"


# Import after class definition to avoid circular imports
InflationRateIndexEnum.model_rebuild()
