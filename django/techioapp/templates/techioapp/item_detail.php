{% extends 'techioapp/index.php' %}


{% block content %}
<div class="col-sm-6 col-md-4">
  <div class="thumbnail">
    <div class="container2">
      <img class="img fadeimage" align = "center" src="http://lenin.pythonanywhere.com/static/{{ item.upload.url }}" alt="Error 404: Image was not found"/>
      <div class="info" style="display:none">
          <p align="center">{{ item.info }}</p>
      </div>
    </div>
    <div class="caption">
      <h3 align="center">{{ item.name }}</h3>
      <p align="center">
        Per piece: €{{ item.price }}, In stock: {{ item.stock }}
      </p>
      <p align="center">
        Amount:<input id=number type="number" min="1" value="1">
        </input>
        {% if user.is_authenticated %}
          <a class="btn btn-default" href="{% url 'item_edit' pk=item.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
        {% endif %}
        <a href="#" class="btn btn-primary addtocartbutton" role="button" data-toggle="modal" data-target="#myModal">Add to cart</a>
      </p>
    </div>
  </div>
</div>
{% endblock %}
