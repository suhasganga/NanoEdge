Version: Next

On this page

> **DeepPartial**<`T`>: `{ [P in keyof T]?: T[P] extends (infer U)[] ? DeepPartial<U>[] : T[P] extends readonly (infer X)[] ? readonly DeepPartial<X>[] : DeepPartial<T[P]> }`

Represents a type `T` where every property is optional.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **T**