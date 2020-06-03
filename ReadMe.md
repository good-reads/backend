# Main Page

### info
1. profile get api
    - POST req
        * user_id or user_email
    - res
        * thumbnail img url
        * user name
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
        * user_id or user_email
    - res
        * logout id or e-mail


### Rate or Review

##### info
1. profile get api
    - POST req
        * user_id or user_email
    - res
        * thumbnail img url
        * user name
1. my list get api
    - POST req
        * user_id or user_email
    - res
        * book names
1. book info get api
    - GET req
        * book_id
    - res
        * book cover img
        * book title
        * book author
        * book rate
        * book review

##### button
1. review submit api
    - POST req
        * book_id
        * review
    - res
1. rate submit api
    - POST req
        * book_id
        * rate


### Search Page

##### info
1. profile get api
    - POST req
        * user_id or user_email
    - res
        * thumbnail img url
        * user name
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

##### search
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
        
##### book list
1. selected book info get api
    - GET req
        * book_id
    - res
        * book cover img
        * book title
        * book author
        * book rate
        * book review
        
### Detail Page

##### info
1. profile get api
    - POST req
        * user_id or user_email
    - res
        * thumbnail img url
        * user name
1. my list get api
    - POST req
        * user_id or user_email
    - res
        * book names
1. book info get api
    - GET req
        * book_id
    - res
        * book cover img
        * book title
        * book author
        * book rate
        * book review

##### my list edit down menu
1. add book in list api
    * POST req
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


### SignUp Page

##### button
1. register info submit api
    * POST req
        - user_email
        - password
    * res
        - token
        

### Login Page

##### button
1. login info submit api
    * POST req
        - user_email
        - password
    * res
        * token


### Add New Book

##### info
1. profile get api
    - POST req
        * user_id or user_email
    - res
        * thumbnail img url
        * user name
1. my list get api
    - POST req
        * user_id or user_email
    - res
        * book names

##### button
1. book info submit api
    - POST req
        * book title
        * book author
        * book thumbnail img
        * book rate
        * book review
    - res
    