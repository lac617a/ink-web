# def productsViews(request):
#   qs = Products.objects.filter(pdState=True)
#   return render(request,'products.html',{'qs':qs})

# def productsHidden(request):
#   get_hide = Products.objects.filter(pdState=False)
#   print(get_hide)
#   return render(request,'products/hide-products.html',{'query':get_hide})

# def productDelete(request,id):
#   get_item = get_object_or_404(Products,pk=id)
#   if request.method == 'POST':
#     get_item.delete()
#     return redirect("Main:pro")
#   return render(request,'products/delete-product.html',{'product':get_item})

# def productEdit(request,id):
#   pro_form = None
#   error = None
#   try:
#     get_product = Products.objects.get(pk=id)
#     if request.method == 'GET':
#       pro_form = ProductsForm(instance=get_product)
#     else:
#       pro_form = ProductsForm(request.POST,instance=get_product)
#       if pro_form.is_valid():
#         pro_form.save()
#       return redirect('Product:pro')
#   except ObjectDoesNotExist as e:
#     error =  e
#   return render(request,
#   'products/edit-product.html',
#   {'query':pro_form,'error':error})
