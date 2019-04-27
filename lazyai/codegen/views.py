from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail

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

    Parameters
    ==========

    The parameters obtained from request are listed below,

    layers : The number of layers in the neural network.
    l_i    : The type of the ith layer. See the list of currently,
             supported layers.
    n_i    : Number of units/nodes in the ith layer.
    email  : The email to which the generated code is to be sent.
             By default, null string.

    Returns
    =======

    The parameters returned in the context are given below,

    'code' : The generated code of the model.

    Supported Layers
    ================
    Format : '.. [<type>] <name>'
    .. [1] Dense
    .. [2] Conv2D
    .. [3] Conv3D
    .. [4] LSTM
    .. [5] Activation
           .. [1] relu
           .. [2] sigmoid
           .. [3] tanh

    Notes
    =====

    The 'return_state' and 'return_sequences' are by default set to True.
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
