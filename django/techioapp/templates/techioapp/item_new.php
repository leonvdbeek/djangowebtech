{% extends 'techioapp/index.php' %}

{% block content %}
    <h1>New item</h1>
    <form enctype="multipart/form-data" class="bs-example form-horizontal" method="POST" >{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-default">Save</button>
    </form>
{% endblock %}
