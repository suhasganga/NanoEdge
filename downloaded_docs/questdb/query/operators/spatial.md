On this page

This page describes the available operators to perform spatial
calculations. For more information on this type of data, see the
[geohashes documentation](/docs/query/datatypes/geohashes/) and the
[spatial functions documentation](/docs/query/functions/spatial/) which have been added to help with filtering and generating data.

### within[​](#within "Direct link to within")

`within(geohash, ...)` - evaluates if a comma-separated list of geohashes are
equal to or within another geohash.

By default, the operator follows normal syntax rules, and `WHERE` is executed before `LATEST ON`. The filter is
compatible with parallel execution in most cases.

note

In QuestDB 8.3.2, the `within` implementation was upgraded, and now supports general `WHERE` filtering.

The prior implementation executed `LATEST ON` before `WHERE`, only supported geohashed constants, and all involved symbol
columns had to be indexed. However, it is highly optimised for that specific execution and uses SIMD instructions.

To re-enable this implementation, you must set `query.within.latest.by.optimisation.enabled=true` in server.conf.

#### Arguments[​](#arguments "Direct link to Arguments")

* `geohash` is a geohash type in text or binary form

#### Returns[​](#returns "Direct link to Returns")

* evaluates to `true` if geohash values are a prefix or complete match based on
  the geohashes passed as arguments

#### Examples[​](#examples "Direct link to Examples")

example geohash filter[Demo this query](https://demo.questdb.io/?query=(%0ASELECT%20pickup_datetime%2C%20%0A%20%20%20%20%20%20%20make_geohash(pickup_latitude%2C%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20pickup_longitude%2C%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%2060)%20pickup_geohash%0AFROM%20trips%0ALIMIT%205%0A)%0AWHERE%20pickup_geohash%20WITHIN%20(%23dr5ru)%3B&executeQuery=true)

```prism-code
(  
SELECT pickup_datetime,   
       make_geohash(pickup_latitude,   
                    pickup_longitude,   
                    60) pickup_geohash  
FROM trips  
LIMIT 5  
)  
WHERE pickup_geohash WITHIN (#dr5ru);
```

Given a table with the following contents:

| ts | device\_id | g1c | g8c |
| --- | --- | --- | --- |
| 2021-09-02T14:20:07.721444Z | device\_2 | e | ezzn5kxb |
| 2021-09-02T14:20:08.241489Z | device\_1 | u | u33w4r2w |
| 2021-09-02T14:20:08.241489Z | device\_3 | u | u33d8b1b |

The `within` operator can be used to filter results by geohash:

```prism-code
SELECT * FROM pos  
WHERE g8c within(#ezz, #u33d8)  
LATEST ON ts PARTITON BY uuid;
```

This yields the following results:

| ts | device\_id | g1c | g8c |
| --- | --- | --- | --- |
| 2021-09-02T14:20:07.721444Z | device\_2 | e | ezzn5kxb |
| 2021-09-02T14:20:08.241489Z | device\_3 | u | u33d8b1b |

Additionally, prefix-like matching can be performed to evaluate if geohashes
exist within a larger grid:

```prism-code
SELECT * FROM pos  
WHERE g8c within(#u33)  
LATEST ON ts PARTITON BY uuid;
```

| ts | device\_id | g1c | g8c |
| --- | --- | --- | --- |
| 2021-09-02T14:20:08.241489Z | device\_1 | u | u33w4r2w |
| 2021-09-02T14:20:08.241489Z | device\_3 | u | u33d8b1b |