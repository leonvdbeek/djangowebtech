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
            <li ><a href="{% url 'item_list' %}">Home</a></li>
            <li ><a href="{% url 'howdoesitwork' %}">How does it work?</a></li>
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li class="active"><a class="glyphicon glyphicon-shopping-cart cartbutton" href="{% url 'shoppingcart' %}"></a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

<!--- End of the navbar --->
<div id="wrap">
  <div id="main" class="container-fluid">
    <div class="container">
	<div class="row">
		<div class="col-xs-12">
			<div class="panel panel-info">
				<div class="panel-heading">
					<div class="panel-title">
						<div class="row">
							<div class="col-xs-6">
								<h5><span class="glyphicon glyphicon-shopping-cart"></span> Shopping Cart</h5>
							</div>
							<div class="col-xs-6">
								<a href="{% url 'item_list' %}" class="btn btn-primary btn-sm btn-block">
									<span class="glyphicon glyphicon-share-alt"></span> Continue shopping
								</a>
							</div>
						</div>
					</div>
				</div>
				<div class="panel-body">
					<div class="row">
						<div class="col-xs-2"><img class="img-responsive" src="http://lenin.pythonanywhere.com/static/djangowebtech/django/techioapp/static/img/arduinonano.jpg">
						</div>
						<div class="col-xs-4">
							<h4 class="product-name"><strong>Arduino Nano</strong></h4><h4><small>This is a smaller version of the well-known Arduino Uno. It is the core of many DIY projects because of its low cost and high efficiency.</small></h4>
						</div>
						<div class="col-xs-6">
							<div class="col-xs-6 text-right">
								<h6><strong>€ 2.00 <span class="text-muted">x</span></strong></h6>
							</div>
							<div class="col-xs-4">
								<input type="text" class="form-control input-sm" value="1">
							</div>
							<div class="col-xs-2">
								<button type="button" class="btn btn-link btn-xs">
									<span class="glyphicon glyphicon-trash"> </span>
								</button>
							</div>
						</div>
					</div>
					<hr>
					<div class="row">
						<div class="col-xs-2"><img class="img-responsive" src="http://lenin.pythonanywhere.com/static/djangowebtech/django/techioapp/static/img/servo.jpg">
						</div>
						<div class="col-xs-4">
							<h4 class="product-name"><strong>Strong servo</strong></h4><h4><small>This is a normal sized servo with high torque. Very usefull for making stuff move certain angles or modify it for continuous rotation so you have a very high torque motor!</small></h4>
						</div>
						<div class="col-xs-6">
							<div class="col-xs-6 text-right">
								<h6><strong>€ 6.75 <span class="text-muted">x</span></strong></h6>
							</div>
							<div class="col-xs-4">
								<input type="text" class="form-control input-sm" value="1">
							</div>
							<div class="col-xs-2">
								<button type="button" class="btn btn-link btn-xs">
									<span class="glyphicon glyphicon-trash"> </span>
								</button>
							</div>
						</div>
					</div>
					<hr>
					<div class="row">
						<div class="text-center">
							<div class="col-xs-9">
								<h6 class="text-right">Added items?</h6>
							</div>
							<div class="col-xs-3">
								<button type="button" class="btn btn-default btn-sm btn-block">
									Update cart
								</button>
							</div>
						</div>
					</div>
				</div>
				<div class="panel-footer">
					<div class="row text-center">
						<div class="col-xs-9">
							<h4 class="text-right">Total <strong>€ 8,75</strong></h4>
						</div>
						<div class="col-xs-3">
							<button type="button" class="btn btn-success btn-block">
								Checkout
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
  </div>
</div>

<!--- footer --->
</div>
</div>
<footer id="footer" class="footer">
  <div class="container">
    <p>
      Designed and built with all the love in the world by 'Lenin' for the course WebTechnology (2ID50) at the Eindhoven University of Technology.
    </p>
    <p align="center">
      Copyright © 2017 'Lenin'
    </p>
  </div>
</footer>

<!--- end of footer --->

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/techiojs.js"></script>
  </body>
</html>
