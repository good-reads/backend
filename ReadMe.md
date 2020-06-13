# Main Page

### info
1. profile get api
    - GET req
        * URL: http://<<server-domain>>/api/accounts/auth/account/get/
        * Authorization: Token <<token>>
    - res
        * code 200: OK
            * name
            * email
            * mylist
                - book_id
                - title
                - author
                - rate
                - thumbnail url
1. my list get api
    - POST req
        * user_id or user_email
    - res
        * book names
1. 인기있는 책 list get api
    - GET req
    - res
        * book names
        * thumbnail img urls
1. 최근 사람들이 읽은 책 list api
    - GET req
    - res
        * book names
        * thumbnail img urls

### search
1. GET method search api
    - GET req
        * genre
        * rate
        * ..
    - res
        * book names
        * author names
        * thumbnail imgs
        * book rates
    
### button
1. logout api
    - POST req
        * URL: http://<<server-domain>>/api/accounts/auth/logout/
        * Authorization: Token <<token>>
    - res
        * code 204: no content


# Rate or Review

### info
1. profile get api
    - GET req
        * URL: http://<<server-domain>>/api/accounts/auth/account/get/
        * Authorization: Token <<token>>
    - res
        * code 200: OK
            * name
            * email
            * mylist
                - book_id
                - title
                - author
                - rate
                - thumbnail url
1. my list get api
    - POST req
        * user_id or user_email
    - res
        * book names
1. book info get api
    - GET req
        * URL: http://<<server-domain>>/api/books/get/details/?book_id=<<number>>
    - res
        * code 200: OK
            * title
            * author
            * intro
            * rate
            * thumbnail
            * img

### button
1. review submit api
    - POST req
        * book_id
        * review
    - res
1. rate submit api
    - POST req
        * book_id
        * rate


# Search Page

### info
1. profile get api
    - GET req
        * URL: http://<<server-domain>>/api/accounts/auth/account/get/
        * Authorization: Token <<token>>
    - res
        * code 200: OK
            * name
            * email
            * mylist
                - book_id
                - title
                - author
                - rate
                - thumbnail url
1. my list get api
    - POST req
        * user_id or user_email
    - res
        * book names
1. book list get api
    - GET req
    - res
        * book titles
        * book thumbnail img urls
        * book authors
        * book rates

### search
1. GET method search api
    - GET req
        * genre
        * rate
        * ..
    - res
        * book names
        * author names
        * thumbnail imgs
        * book rates
        
### book list
1. selected book info get api
    - GET req
        * URL: http://<<server-domain>>/api/books/get/details/?book_id=<<number>>
    - res
        * code 200: OK
            * title
            * author
            * intro
            * rate
            * thumbnail
            * img
        
# Detail Page

### info
1. profile get api
    - GET req
        * URL: http://<<server-domain>>/api/accounts/auth/account/get/
        * Authorization: Token <<token>>
    - res
        * code 200: OK
            * name
            * email
            * mylist
                - book_id
                - title
                - author
                - rate
                - thumbnail url
1. my list get api
    - POST req
        * user_id or user_email
    - res
        * book names
1. book info get api
    - GET req
        * URL: http://<<server-domain>>/api/books/get/details/?book_id=<<number>>
    - res
        * code 200: OK
            * title
            * author
            * intro
            * rate
            * thumbnail
            * img

### my list edit down menu
1. add book in list api
    * PATCH req
        - URL: http://<<server-domain>>/api/accounts/auth/mylist/edit/
        - Authorization: Token <<token>>
            - user_id
            - book_id
            - list_id
    * res
1. create new list api
    * POST req
        - user_id
        - book_id
        - list_name
    * res


# SignUp Page

### button
1. register info submit api
    * POST req 
        - URL: http://<<server-domain>>/api/accounts/auth/register/
            * name
            * email
            * password
    * res
        - code 201: created
1. password change api
    * POST req
        - URL: http://<<server-domain>>/api/accounts/auth/account/update/
        - Authorization: Token <<token>>
            * password
    * res
        - code 200
        

# Login Page

### button
1. login info submit api
    * POST req
        - URL: http://<<server-domain>>/api/accounts/auth/login/
            - email
            - password
    * res
        * code 200: OK
            * user_id
            * token


# Add New Book

### info         
1. profile get api
    - GET req
        * URL: http://<<server-domain>>/api/accounts/auth/account/get/
        * Authorization: Token <<token>>
    - res
        * code 200: OK
            * name
            * email
            * mylist
                - book_id
                - title
                - author
                - rate
                - thumbnail url

### button
1. book info submit api
    - PUT req
        * URL: http://<<server-domain>>/api/books/register/
        * Authorization: Token <<token>>
            * book title
            * book author
            * book thumbnail img
            * book rate
            * book intro
    - res
        * code 201: created

# My Page

### button
1. change user info api
    - PATCH req
        * URL: http://<<server-domain>>/api/accounts/auth/account/update/
        * Authorization: Token <<token>>
            * user_email
            * user_name
            * thumbnail img
            * .. (except password)
    - res
        * code 202: Accepted
            * what you changed
1. password change api
    * POST req
        - URL: http://<<server-domain>>/api/accounts/auth/account/update/
        - Authorization: Token <<token>>
            * password
    * res
        - code 200: OK