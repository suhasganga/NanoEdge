Version: 5.1

On this page

> **Nominal**<`T`, `Name`>: `T` & `object`

This is the generic type useful for declaring a nominal type,
which does not structurally matches with the base type and
the other types declared over the same base type

## Examples[​](#examples "Direct link to Examples")

```prism-code
type Index = Nominal<number, 'Index'>;  
// let i: Index = 42; // this fails to compile  
let i: Index = 42 as Index; // OK
```

```prism-code
type TagName = Nominal<string, 'TagName'>;
```

## Type declaration[​](#type-declaration "Direct link to Type declaration")

### [species][​](#species "Direct link to [species]")

> **[species]**: `Name`

The 'name' or species of the nominal.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **T**

• **Name** *extends* `string`