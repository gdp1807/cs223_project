from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
# Create your views here.
def home(request):
    """
    Renders the home.html template.
    """
    template = loader.get_template('codegen/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def generate(request):
    """
    Renders the generate.html template.
    """
    template = loader.get_template('codegen/generate.html')
    context = {}
    return HttpResponse(template.render(context, request))

def output(request):
    """
    Renders the output.html template.
    """
    num_layers, layers, nodes = int(request.GET["layers"]), [], []
    activations = {'1': 'relu', '2': 'sigmoid', '3': 'tanh'}
    code = "import keras.layers as kl\n\n"
    code += "def model(n_input, n_output):\n"
    code += "    input = Input(shape = (n_input))\n"
    for l in range(num_layers):
        type = int(request.GET["l" + str(l)])
        num = str(request.GET["n"+str(l)])
        if type == 1:
            code += "    out = kl.Dense(" + num + ")(input)\n"
        elif type == 2:
            code += "    out = kl.Conv2D(" + num + ", 1)(out)\n"
        elif type == 3:
            code += "    out = kl.Conv3D(" + num + ", 1)(out)\n"
        elif type == 4:
            code += "    out = kl.LSTM(" + num + ", return_state=True, return_sequences "\
                    "=True)(out)\n"
        elif type == 5:
            ac_type = activations[num]
            code += "   out = kl.Activation('"+ ac_type +"')(out)\n"
    template = loader.get_template('codegen/output.html')
    context = {'code': code}
    email = request.GET["email"]
    if email != "":
        send_mail(
            'Code by LazyAI',
            "Hey " + email.split('@')[0] + "\nThe code for your model,\n" +\
            code + '\n' + 'Regards,\nLazyAI Team',
            'czgdp1807@gmail.com',
            [email],
            fail_silently = False,
        )
    return HttpResponse(template.render(context, request))
