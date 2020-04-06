## Research Summary
* No *official* standalone Django ORM
* **BUT** Django built to be very loosely coupled - few assumptions about it's use
* There are multiple Git Repo examples of using Django-ORM as a standlone
* All threads I've found of people asking about standalone Django-ORM have responded with examples (None have said you cannot or even not recommended it - implying there shouldn't be an issue doing so)
* Lots of code snippets on Stackoverflow on how to use ORM without any Web component

## Links + key info

* **[1]** *Thread - 4y/o*: "How to use Django 1.8.5 **ORM without** creating a **django project?**" [link >](https://stackoverflow.com/questions/33170016/how-to-use-django-1-8-5-orm-without-creating-a-django-project)
  * Top answer outlines a structure of how to set this up
* **[2]** *Repo- 3y/o*: "Django-ORM **Standalone Template**" [link >](https://github.com/dancaron/Django-ORM)
  * "This is a Django project template that allows you to use the **database component** of Django **without** having to use **the rest of Django** (i.e. running a web server)."
* **[3]** *Thread - 1y/o*: "Using Django Models standalone client-sided" [link >](https://www.reddit.com/r/django/comments/9hj2ru/using_django_models_standalone_clientsided/)
  * User: askes if they can have a client which populates a Django object and sends this to a server
    * They want a lightweight client and thereby don't want to install Django
    * This is different from our requirements, but top answer relevant:
  * Top answer: states there is **no official standalone Django ORM** BUT points to examples of people using ORM with other functionality
    * Specifically, they point to 11y/o thread (below)
* **[4]** *Thread - 11y/o*: "Use only some parts of Django?" [link >](https://stackoverflow.com/questions/302651/use-only-some-parts-of-django)
  * User: wants to use the following Django components: models, DB, and caching API; BUT NOT templating, urlconfigs, html/http
  * Top answer: describes how **they use Django for object/DB without urlconfigs**
    * provides code snippets of how to do so
  * Second answer: points out that Django prides itself on it's loose coupling, the framework makes minimal assumptions about how it is used.
    * Specifically, for example, Django models (and templates) know nothing about HTML/HTTP
