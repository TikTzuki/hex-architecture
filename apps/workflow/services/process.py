from apps.workflow.schemas.document import Document
from apps.workflow.services.states.has_approve_level import HasApproveLevel
from apps.workflow.services.states.has_approver import HasApprover


def phan_bo_user(user_cpd, user_cks, doc: Document):
    # init
    doc = Document(HasApproveLevel(doc))
    print(
        doc.state.accessible_permissions
    )
    # process
    doc.set_state(HasApprover(doc, user_cpd, user_cks))
    print(
        doc.state.accessible_permissions
    )
    # dost


phan_bo_user("cpd", "cks", Document(None))
