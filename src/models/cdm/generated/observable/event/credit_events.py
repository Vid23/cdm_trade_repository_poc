from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.observable.event.credit_event_notice import CreditEventNotice
    from src.models.cdm.generated.observable.event.failure_to_pay import FailureToPay
    from src.models.cdm.generated.observable.event.restructuring import Restructuring

class CreditEvents(CdmModelBase):
    """A class to specify the applicable Credit Events that would trigger a settlement, as specified in the related Confirmation and defined in the ISDA 2014 Credit Definition article IV section 4.1."""
    bankruptcy: bool = Field(None, description="A credit event. The reference entity has been dissolved or has become insolvent. It also covers events that may be a precursor to insolvency such as instigation of bankruptcy or insolvency proceedings. Sovereign trades are not subject to Bankruptcy as 'technically' a Sovereign cannot become bankrupt. ISDA 2003 Term: Bankruptcy.")
    failure_to_pay: ForwardRef("FailureToPay") = Field(None, description="A credit event. This credit event triggers, after the expiration of any applicable grace period, if the reference entity fails to make due payments in an aggregate amount of not less than the payment requirement on one or more obligations (e.g. a missed coupon payment). ISDA 2003 Term: Failure to Pay.")
    failure_to_pay_principal: bool = Field(None, description="A credit event. Corresponds to the failure by the Reference Entity to pay an expected principal amount or the payment of an actual principal amount that is less than the expected principal amount. ISDA 2003 Term: Failure to Pay Principal.")
    failure_to_pay_interest: bool = Field(None, description="A credit event. Corresponds to the failure by the Reference Entity to pay an expected interest amount or the payment of an actual interest amount that is less than the expected interest amount. ISDA 2003 Term: Failure to Pay Interest.")
    obligation_default: bool = Field(None, description="A credit event. One or more of the obligations have become capable of being declared due and payable before they would otherwise have been due and payable as a result of, or on the basis of, the occurrence of a default, event of default or other similar condition or event other than failure to pay. ISDA 2003 Term: Obligation Default.")
    obligation_acceleration: bool = Field(None, description="A credit event. One or more of the obligations have been declared due and payable before they would otherwise have been due and payable as a result of, or on the basis of, the occurrence of a default, event of default or other similar condition or event other than failure to pay (preferred by the market over Obligation Default, because more definitive and encompasses the definition of Obligation Default - this is more favorable to the Seller). Subject to the default requirement amount. ISDA 2003 Term: Obligation Acceleration.")
    repudiation_moratorium: bool = Field(None, description="A credit event. The reference entity, or a governmental authority, either refuses to recognise or challenges the validity of one or more obligations of the reference entity, or imposes a moratorium thereby postponing payments on one or more of the obligations of the reference entity. Subject to the default requirement amount. ISDA 2003 Term: Repudiation/Moratorium.")
    restructuring: ForwardRef("Restructuring") = Field(None, description="A credit event. A restructuring is an event that materially impacts the reference entity's obligations, such as an interest rate reduction, principal reduction, deferral of interest or principal, change in priority ranking, or change in currency or composition of payment. ISDA 2003 Term: Restructuring.")
    governmental_intervention: bool = Field(None, description="A credit event. A governmental intervention is an event resulting from an action by a governmental authority that materially impacts the reference entity's obligations, such as an interest rate reduction, principal reduction, deferral of interest or principal, change in priority ranking, or change in currency or composition of payment. ISDA 2014 Term: Governmental Intervention.")
    distressed_ratings_downgrade: bool = Field(None, description="A credit event. Results from the fact that the rating of the reference obligation is down-graded to a distressed rating level. From a usage standpoint, this credit event is typically not applicable in case of RMBS trades.")
    maturity_extension: bool = Field(None, description="A credit event. Results from the fact that the underlier fails to make principal payments as expected.")
    writedown: bool = Field(None, description="A credit event. Results from the fact that the underlier writes down its outstanding principal amount.")
    implied_writedown: bool = Field(None, description="A credit event. Results from the fact that losses occur to the underlying instruments that do not result in reductions of the outstanding principal of the reference obligation.")
    default_requirement: ForwardRef("Money") = Field(None, description="In relation to certain credit events, serves as a threshold for Obligation Acceleration, Obligation Default, Repudiation/Moratorium and Restructuring. Market standard is USD 10,000,000 (JPY 1,000,000,000 for all Japanese Yen trades). This is applied on an aggregate or total basis across all Obligations of the Reference Entity. Used to prevent technical/operational errors from triggering credit events. ISDA 2003 Term: Default Requirement.")
    credit_event_notice: ForwardRef("CreditEventNotice") = Field(None, description="A specified condition to settlement. An irrevocable written or verbal notice that describes a credit event that has occurred. The notice is sent from the notifying party (either the buyer or the seller) to the counterparty. It provides information relevant to determining that a credit event has occurred. This is typically accompanied by Publicly Available Information. ISDA 2003 Term: Credit Event Notice.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.observable.event.credit_event_notice import CreditEventNotice
from src.models.cdm.generated.observable.event.failure_to_pay import FailureToPay
from src.models.cdm.generated.observable.event.restructuring import Restructuring
CreditEvents.model_rebuild()
