# Naming

* Don't encode names
  * `dt = ` vs `delay_in_seconds = `
* Don't use type in naming
  * `n_apples`, `s_name` (Hungarian notation)
  * `df_courses`
  * `user_list`
  * Let the IDE handle types
  * These can lie (eg. `user_list` is a dictionary)
* Put information into names
  * `time_since_heartbeat` vs `seconds_since_heartbeat`
  * Dont use false information
  * Don't use meaningless information:
    * `transform_data(a1, a2)` vs.
    * `transfomr_data(source, destination)`
* Length should reflet scope
  * `i` in loops is ok (but not `l` or `o`, they're similar to 1 and 0)
  * `days` in local scope
  * `days_from_customer_registration` in larger scopes
* Avoid mental maps
  * Don't use language elements/shadows
  * Don't use mental maps for common names
    * `dataframe` vs `in_table`
* Make variables searchable
* Don't use puns
* Use domain/solution names

Use nouns for classes and variables, verbs for functions.