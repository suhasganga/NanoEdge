##### [http::basic\_fields::clear](clear.html "http::basic_fields::clear")

Remove all fields from the container.

###### [Synopsis](clear.html#beast.ref.boost__beast__http__basic_fields.clear.synopsis)

```programlisting
void
clear();
```

###### [Description](clear.html#beast.ref.boost__beast__http__basic_fields.clear.description)

All references, pointers, or iterators referring to contained elements
are invalidated. All past-the-end iterators are also invalidated.

###### [Postconditions:](clear.html#beast.ref.boost__beast__http__basic_fields.clear.postconditions)

```programlisting
std::distance(this->begin(), this->end()) == 0
```