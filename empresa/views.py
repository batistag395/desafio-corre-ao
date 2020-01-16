from django.shortcuts import render

# Create your views here.
def cadastro(request):
    form = EmpresaForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args['msg'] = 'Cadastro Realizado com sucesso'
    return render(request, 'cad-Empresa.html', args)