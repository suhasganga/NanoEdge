##### [http::message::clear](clear.html "http::message::clear")

(Inherited from [`http::basic_fields`](../boost__beast__http__basic_fields.html "http::basic_fields"))

Remove all fields from the container.

###### [Synopsis](clear.html#beast.ref.boost__beast__http__message.clear.synopsis)

```programlisting
void
clear();
```

###### [Description](clear.html#beast.ref.boost__beast__http__message.clear.description)

All references, pointers, or iterators referring to contained elements
are invalidated. All past-the-end iterators are also invalidated.

###### [Postconditions:](clear.html#beast.ref.boost__beast__http__message.clear.postconditions)

```programlisting
std::distance(this->begin(), this->end()) == 0
```