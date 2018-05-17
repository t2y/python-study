from __future__ import annotations

class C:
    field = 'c_field'
    def method(self) -> C.field:...  # this is OK

    def method(self) -> field:...  # this is OK

    def method(self) -> C.D:...  # this is OK

    def method(self) -> D:...  # this is OK

    class D:
        field2 = 'd_field'
        def method(self) -> C.D.field2:...  # this is OK

        def method(self) -> D.field2:...  # this is OK

        def method(self) -> field2:...  # this is OK

        def method(self) -> field:...  # this FAILS, class D doesn't
                                       # see C's attributes,  This was
                                       # already true before this PEP.
