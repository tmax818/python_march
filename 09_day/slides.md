![](../images/coding_dojo_logo_white.png)
<!-- .slide:data-background="#000000" -->

---
<!-- .slide:data-background="#000000" -->
# CRUD Continued
---
## MVC
--
![](../images/mvc.png)
<!-- .element: data-trim class="r-stretch r-fit-text" -->
--
![](../images/mvc2.png)
<!-- .element: data-trim class="r-stretch r-fit-text" -->
---
## Modularization
--
### We started with three files
1. `server.py`   <!-- .element: class="fragment" -->
2. `mysqlconnection.py`   <!-- .element: class="fragment" -->
3. `model.py`   <!-- .element: class="fragment" -->

--
### Our file structure looked like this:
![](../images/pre-mod.png)
<!-- .element:class="r-stretch" -->
<!-- .element:class="fragment" -->
--
![](../images/mod1.png)
--
![](../images/mod2.png)
--
![](../images/mod3.png)
--
![](../images/mod4.png)
--
![](../images/mod5.png)
--
![](../images/mod6.png)
--
![](../images/mod7.png)
---
## Controllers
--
## Controllers
- controllers handle routes/requests and <!-- .element: class="fragment" -->
- minimal logic (fat models, skinny controllers) <!-- .element: class="fragment" -->
- access database via models <!-- .element: class="fragment" -->
---
## Models
--
## Models
- models handles logic related to data <!-- .element: class="fragment" -->
- access database via mysqlconnection.py <!-- .element: class="fragment" -->
---
## User's CRUD Modularized
---
## relationships
---
## dojos and ninjas (core)
---
## relationships advanced
---
## circular imports
---
## books (practice)
---
## friendships (optional)

