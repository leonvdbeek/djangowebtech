{% load staticfiles %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Tech.io components</title>
    <link href="{% static 'css/bootstrap.min.css'%}" rel="stylesheet">
    <link href="{% static 'css/techiocss.css'%}" rel="stylesheet">

  </head>
  <body>

<!--- this is the nav bar --->
<nav class="navbar navbar-default navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        <a class="navbar-brand" href="{% url 'item_list' %}">
          <strong> Tech.io</strong>
        </a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="{% url 'item_list' %}">Home</a></li>
            <li><a href="howdoesitwork">How does it work?</a></li>
            <li>
              {% if user.is_authenticated %}
                  <a href="{% url 'item_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span> Add new Items</a>
              {% endif %}
            </li>
          </ul>

          <ul class="nav navbar-nav navbar-right">
            <li class="navbar-text">
              {% if user.is_authenticated %}
                  You are logged in as an administrator.
              {% endif %}
            </li>
            <li><a class="glyphicon glyphicon-shopping-cart cartbutton" href="shoppingcart"></a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

<!--- End of the navbar --->

<!--- Beginning of jumbotron --->

  <div class="container">
    <div class="jumbotron">
      <h1 align="center">Welcome to Tech.io!</h1>
      <p align="center">On this website we sell all kinds of electronic components that you can use for your projects!</p>
      <p align="center"><a class="btn btn-primary btn-lg" href="howdoesitwork" role="button">How does it work?</a></p>
    </div>
  </div>



<!--- End of jumbotron --->

{% block new_content %}
{% endblock %}


<!--- This is the content oh all the cards --->
<div id="wrap">
  <div id="main" class="container-fluid">
    <div class="container">
      <div class="row">
        {% block content %}
        {% endblock %}
      </div>
    </div>
  </div>
</div>
<!--- End of all the content --->

<!-- Button trigger modal -->


<!-- Modal -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 align="center" class="modal-title" id="myModalLabel">Item(s) succesfully added to cart!</h4>
      </div>
      <div class="modal-body">
        <p align="center">Do you want to continue shopping or go to checkout?</p>
      </div>
      <div class="modal-footer">
        <button align="center" type="button" class="btn btn-default" data-dismiss="modal">continue shopping</button>
        <a href="shoppingcart" class="btn btn-primary btn-sm">Go to checkout
        </a>
      </div>
    </div>
  </div>
</div>


<!--- footer --->
<a name="footer"></a>
<footer id="footer" class="footer">
  <div class="container">
    <p>
      Designed and built with all the love in the world by 'Lenin' for the course WebTechnology (2ID60) at the Eindhoven University of Technology.
    </p>
    <p align="center">
      Copyright © 2017 'Lenin'
    </p>
  </div>
</footer>
<!--- end of footer --->

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="{% static 'js/bootstrap.min.js'%}"></script>
    <script src="{% static 'js/techiojs.js'%}"></script>
  </body>
</html>
