from django.shortcuts import render

# Create your views here.
def mostrar_formulario_cad_empresa(request):
  args = {'msg': ''}
  if request == 'POST':
    empresa = Empresa()
    empresa.nome = request.POST.get('nome')
    empresa.cnpj = request.POST.get('cnpj')
    empresa.email = request.POST.get('email')
    empresa.telefone = request.POST.get('telefone')
    empresa.area = request.POST.get('Area de atuação')
    empresa.save
    return render(request, 'login-empresa.html')
  return render(request, 'cad-empresa.html', args)


def mostrar_empresas(request):
  args = {'msg': ''}
  if request == 'POST': 
    empresa = Empresa.objects()
    empresa.nome = request.POST.get('nome')
    empresa.cnpj = request.POST.get('cnpj')
  
  return render(request, 'empresa.html', args)


def login_empresa(request):
  if request.method == '':
    email_formulario = request.POST.get('email')
    empresa.cnpj = request.POST.get('cnpj')
    empresa_banco_dados = Empresa.objects.filter(email=email_formulario).first()
    if empresa_banco_dados is not None:
      args = {
        'empresa': empresa_banco_dados
      }
      return render(request, 'cadastrar_conta.html', args)
    return render(request, 'login-empresa.html', {'msg': 'Ops, não encontramos'})

  return render(request, 'login-empresa.html', {'msg': 'olá, bem vindo'})