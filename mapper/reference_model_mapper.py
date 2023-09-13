from model.reference_model import ReferenceModel


def reference_model_mapper(reference) -> ReferenceModel:
    return ReferenceModel(
        id=reference.id,
        code=reference.code,
        name=reference.name
    )