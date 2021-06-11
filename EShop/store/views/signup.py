from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('password')

        value = {'first_name': first_name,
                 'last_name': last_name,
                 'phone': phone,
                 'email': email,
                 'password': password,
                 }

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password,
                            )

        error_message = self.validateCustomer(customer)

        # Saving
        if not error_message:

            # customer = Customer(**postData)
            customer.password = make_password(customer.password)
            customer.register()
            # return index(request)
            return redirect('homepage')
        else:

            data = {
                'error': error_message,
                'values': value,
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name req"

        elif len(customer.first_name) < 4:
            error_message = "first name should not be less than 4 char"

        if not customer.last_name:
            error_message = "Last Name req"

        if customer.isExists():
            error_message = "Customer already exists"

        return error_message
