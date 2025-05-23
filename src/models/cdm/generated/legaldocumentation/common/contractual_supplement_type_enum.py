from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ContractualSupplementTypeEnum(CdmModelBase):
    """The enumerated values to define the supplements to a base set of ISDA Definitions that are applicable to the transaction."""
    # Enum values
    ABX: ClassVar[str] = "ABX"
    ABXTranche: ClassVar[str] = "ABXTranche"
    CDSonLeveragedLoans: ClassVar[str] = "CDSonLeveragedLoans"
    CDSonMBS: ClassVar[str] = "CDSonMBS"
    CDX: ClassVar[str] = "CDX"
    CDXEmergingMarkets: ClassVar[str] = "CDXEmergingMarkets"
    CDXEmergingMarketsDiversified: ClassVar[str] = "CDXEmergingMarketsDiversified"
    CDXSwaption: ClassVar[str] = "CDXSwaption"
    CDXTranche: ClassVar[str] = "CDXTranche"
    CMBX: ClassVar[str] = "CMBX"
    EuropeanCMBS: ClassVar[str] = "EuropeanCMBS"
    EuropeanRMBS: ClassVar[str] = "EuropeanRMBS"
    IOS: ClassVar[str] = "IOS"
    ISDA1999CreditConvertibleExchangeableAccretingObligations: ClassVar[str] = "ISDA1999CreditConvertibleExchangeableAccretingObligations"
    ISDA1999CreditRestructuring: ClassVar[str] = "ISDA1999CreditRestructuring"
    ISDA1999CreditSuccessorAndCreditEvents: ClassVar[str] = "ISDA1999CreditSuccessorAndCreditEvents"
    ISDA2003AdditionalProvisionsLPN: ClassVar[str] = "ISDA2003AdditionalProvisionsLPN"
    ISDA2003ContingentCreditSpreadTransaction: ClassVar[str] = "ISDA2003ContingentCreditSpreadTransaction"
    ISDA2003Credit2005MatrixSupplement: ClassVar[str] = "ISDA2003Credit2005MatrixSupplement"
    ISDA2003CreditArgentineRepublic: ClassVar[str] = "ISDA2003CreditArgentineRepublic"
    ISDA2003CreditAuctionSupplement: ClassVar[str] = "ISDA2003CreditAuctionSupplement"
    ISDA2003CreditMay2003: ClassVar[str] = "ISDA2003CreditMay2003"
    ISDA2003CreditMonolineInsurers: ClassVar[str] = "ISDA2003CreditMonolineInsurers"
    ISDA2003CreditMonolineInsurers2005: ClassVar[str] = "ISDA2003CreditMonolineInsurers2005"
    ISDA2003CreditRepublicOfHungary: ClassVar[str] = "ISDA2003CreditRepublicOfHungary"
    ISDA2003CreditRepublicOfHungary2005: ClassVar[str] = "ISDA2003CreditRepublicOfHungary2005"
    ISDA2003CreditRussianFederation: ClassVar[str] = "ISDA2003CreditRussianFederation"
    ISDA2003CreditUSMunicipals: ClassVar[str] = "ISDA2003CreditUSMunicipals"
    ISDA2003STMicroelectronicsNV: ClassVar[str] = "ISDA2003STMicroelectronicsNV"
    ISDA2007FullLookthroughDepositoryReceiptSupplement: ClassVar[str] = "ISDA2007FullLookthroughDepositoryReceiptSupplement"
    ISDA2007PartialLookthroughDepositoryReceiptSupplement: ClassVar[str] = "ISDA2007PartialLookthroughDepositoryReceiptSupplement"
    ISDACreditMonolineInsurers: ClassVar[str] = "ISDACreditMonolineInsurers"
    ISDADeliveryRestrictions: ClassVar[str] = "ISDADeliveryRestrictions"
    ISDAFixedRecovery: ClassVar[str] = "ISDAFixedRecovery"
    ISDALPNReferenceEntities: ClassVar[str] = "ISDALPNReferenceEntities"
    ISDAMarch2004EquityCanadianSupplement: ClassVar[str] = "ISDAMarch2004EquityCanadianSupplement"
    ISDARecoveryLock: ClassVar[str] = "ISDARecoveryLock"
    ISDASecuredDeliverableObligationCharacteristic: ClassVar[str] = "ISDASecuredDeliverableObligationCharacteristic"
    LCDX: ClassVar[str] = "LCDX"
    LCDXTranche: ClassVar[str] = "LCDXTranche"
    MBX: ClassVar[str] = "MBX"
    MCDX: ClassVar[str] = "MCDX"
    PO: ClassVar[str] = "PO"
    PrimeX: ClassVar[str] = "PrimeX"
    StandardCDXTranche: ClassVar[str] = "StandardCDXTranche"
    StandardLCDS: ClassVar[str] = "StandardLCDS"
    StandardLCDSBullet: ClassVar[str] = "StandardLCDSBullet"
    StandardLCDXBullet: ClassVar[str] = "StandardLCDXBullet"
    StandardLCDXBulletTranche: ClassVar[str] = "StandardLCDXBulletTranche"
    StandardiTraxxEuropeTranche: ClassVar[str] = "StandardiTraxxEuropeTranche"
    SyndicatedSecuredLoanCDS: ClassVar[str] = "SyndicatedSecuredLoanCDS"
    TRX: ClassVar[str] = "TRX"
    TRX_II: ClassVar[str] = "TRX.II"
    iTraxxAsiaExJapan: ClassVar[str] = "iTraxxAsiaExJapan"
    iTraxxAsiaExJapanSwaption: ClassVar[str] = "iTraxxAsiaExJapanSwaption"
    iTraxxAsiaExJapanTranche: ClassVar[str] = "iTraxxAsiaExJapanTranche"
    iTraxxAustralia: ClassVar[str] = "iTraxxAustralia"
    iTraxxAustraliaSwaption: ClassVar[str] = "iTraxxAustraliaSwaption"
    iTraxxAustraliaTranche: ClassVar[str] = "iTraxxAustraliaTranche"
    iTraxxCJ: ClassVar[str] = "iTraxxCJ"
    iTraxxCJTranche: ClassVar[str] = "iTraxxCJTranche"
    iTraxxEurope: ClassVar[str] = "iTraxxEurope"
    iTraxxEuropeDealer: ClassVar[str] = "iTraxxEuropeDealer"
    iTraxxEuropeNonDealer: ClassVar[str] = "iTraxxEuropeNonDealer"
    iTraxxEuropeSwaption: ClassVar[str] = "iTraxxEuropeSwaption"
    iTraxxEuropeTranche: ClassVar[str] = "iTraxxEuropeTranche"
    iTraxxJapan: ClassVar[str] = "iTraxxJapan"
    iTraxxJapanSwaption: ClassVar[str] = "iTraxxJapanSwaption"
    iTraxxJapanTranche: ClassVar[str] = "iTraxxJapanTranche"
    iTraxxLevX: ClassVar[str] = "iTraxxLevX"
    iTraxxSDI75Dealer: ClassVar[str] = "iTraxxSDI75Dealer"
    iTraxxSDI75NonDealer: ClassVar[str] = "iTraxxSDI75NonDealer"
    iTraxxSovX: ClassVar[str] = "iTraxxSovX"


# Import after class definition to avoid circular imports
ContractualSupplementTypeEnum.model_rebuild()
