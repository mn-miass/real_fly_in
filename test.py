from typing import Annotated
from pydantic import TypeAdapter, Field
from pydantic._internal._model_construction import ModelMetaclass


class test():
    adapter_name = TypeAdapter(Annotated(str, Field(min_length=3, max_length=10)))
    adapter_age = TypeAdapter(Annotated(int, Field(ge=0, le=150)))
    def __init__(self, name, age) -> None:
        self.name = test.adapter_name.validate_python(name)
        self.age = test.adapter_age.validate_python(age)



d = test("hghg", 12)