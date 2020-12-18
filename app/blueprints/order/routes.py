from . import bp as order
from flask import render_template, url_for, render_template, flash, redirect
from app.forms import OrderForm

@order.route('/order_form')
def order_form():
    form = OrderForm()
    context = {
        'form':form
    }




    return render_template('order_form.html', **context )