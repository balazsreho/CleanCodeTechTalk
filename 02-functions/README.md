# Functions

* Functions should be small
  * Even smaller

* Separation
  * They should only do one thing
  * With no side effect
  * At one abstraction level
    * Error handling should be another level

* Answer or do one thing

>   * **WRONG**: if (set_user("username", "Mike")
>     * Is it set the username to Mike, and return True on success?
>     * Or is it mean that a user named Mike should be exists?
>   * **RIGHT**: change_username("Mike") and is_user_exists("Mike")

* Top to bottom reading
  * Call hierarchy should be read as a story.

> * process_user_report
>   * select_user_and_generate_report
>     * select_user_if_exists
>       * is_user_in_database
>     * generate_report
>       * generate_html
>         * generate_static_templates
>         * generate_user_template
>       * mail_report

* Don't repeat yourself
  * If your code contains similar (but not the same) functions, it's not clean

* Less arguments
  * 0 is preferred
  * 1 or 2 is okay
  * 3 is too much
  * more only in special cases
  * arg* lists are ok (as the read as one list)

> **WRONG**: update_courses_table(db_host, db_port, db_user, db_pass, db_table)
> **RIGHT**: update_courses_table(db_config)

* Bool arguments should be avoided

> **WRONG**: render_report(true)
> **RIGHT**: render_report_with_header() and render_report_without_header()