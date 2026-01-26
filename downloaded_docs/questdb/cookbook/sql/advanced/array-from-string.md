On this page

Cast string literals to array types for use with functions that accept array parameters.

## Solution[​](#solution "Direct link to Solution")

To cast an array from a string you need to cast to `double[]` for a vector, or to `double[][]` for a two-dimensional array. You can just keep adding brackets for as many dimensions as the literal has.

This query shows how to convert a string literal into an array, even when there are new lines:

Cast string to array[Demo this query](https://demo.questdb.io/?query=SELECT%20CAST('%5B%0A%20%20%5B%201.0%2C%202.0%2C%203.0%20%5D%2C%0A%20%20%5B%0A%20%20%20%204.0%2C%0A%20%20%20%205.0%2C%0A%20%20%20%206.0%0A%20%20%5D%0A%5D'%20AS%20double%5B%5D%5B%5D)%2C%0Acast('%5B%5B1%2C2%2C3%5D%2C%5B4%2C5%2C6%5D%5D'%20as%20double%5B%5D%5B%5D)%3B&executeQuery=true)

```prism-code
SELECT CAST('[  
  [ 1.0, 2.0, 3.0 ],  
  [  
    4.0,  
    5.0,  
    6.0  
  ]  
]' AS double[][]),  
cast('[[1,2,3],[4,5,6]]' as double[][]);
```

Note if you add the wrong number of brackets (for example, in this case if you try casting to `double[]` or `double[][][][]`), it will not error, but will instead convert as null.

Related Documentation

* [CAST function](/docs/query/sql/cast/)
* [Data types](/docs/query/datatypes/overview/)