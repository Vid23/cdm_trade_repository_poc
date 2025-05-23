from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_portfolio_state import ReferenceWithMetaPortfolioState
    from src.models.cdm.generated.metafields.reference_with_meta_trade import ReferenceWithMetaTrade
    from src.models.cdm.generated.metafields.reference_with_meta_workflow_step import ReferenceWithMetaWorkflowStep

class Lineage(CdmModelBase):
    """A class to provide lineage information across lifecycle events through a pointer or set of pointers into the event(s), contract(s) and, possibly, payout components that the event is dependent on or relates to. As an example, if an contractFormation event is corrected, the correction event will have a lineage into the initial event, which takes the form of a globalKey into that initial contract formation event. Two referencing mechanisms are provided as part of the CDM: either the globalKey, which corresponds to the hash value of the CDM class which is referred to, or a reference qualifier which is meant to provide support for the ingestion of xml documents with id/href mechanisms. The CDM recommends the use of the globalKey and provides a default implementation which is accessible in the generated code through org.isda.cdm.globalKey.GlobalKeyHashCalculator. If implementers want to use an alternative hashing mechanism, the API in which they need to plug it is com.rosetta.model.lib.HashFunction."""
    trade_reference: List[ForwardRef("ReferenceWithMetaTrade")] = Field(None)
    event_reference: List[ForwardRef("ReferenceWithMetaWorkflowStep")] = Field(None, description="The reference to the instantiation of an Event object, either through a globalKey or an xml-derived id/href mechanism. The definition associated to the Lineage class provides more details with respect to those referencing approaches, their expected usage and available implementation.")
    portfolio_state_reference: List[ForwardRef("ReferenceWithMetaPortfolioState")] = Field(None, description="The reference to the previous state of a Portfolio, in a chain of Events leading up to a build of that Portfolio as the holding of Product(s) in specific Quantity(ies). As part of the PortfolioState object, a pointer to the previous PortfolioState is provided through a Lineage object, together with pointer(s) to the Event or set of Events leading up to the current (new) state.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_portfolio_state import ReferenceWithMetaPortfolioState
from src.models.cdm.generated.metafields.reference_with_meta_trade import ReferenceWithMetaTrade
from src.models.cdm.generated.metafields.reference_with_meta_workflow_step import ReferenceWithMetaWorkflowStep
Lineage.model_rebuild()
