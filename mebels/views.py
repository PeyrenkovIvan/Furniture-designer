from django.shortcuts import render , redirect
from django.http import HttpResponse ,JsonResponse
from django.db.models import Q
from .models import Bed
from .forms import BedForm
from django.views.decorators.csrf import csrf_protect
from django.utils import translation
from django.utils.translation import activate
from .translation import PARAMETER_TRANSLATIONS

@csrf_protect
def index(request):

# Text Result(submit)
	# filted_result = []


	# if request.method == 'POST':
	# 	bed = BedForm(request.POST)
	# 	if bed.is_valid():
	# 		lenght = bed.cleaned_data['lenght'] 
	# 		width = bed.cleaned_data['width']
	# 		base = bed.cleaned_data['base']
	# 		color = bed.cleaned_data['color']
			
	# 		result = Bed.objects.all()

	# 		fil_lenght = Q(lenght=lenght)if lenght else Q()
	# 		fil_width = Q(width=width)if width else Q()
	# 		fil_base = Q(base=base)if base else Q()
	# 		fil_color = Q(color=color)if color else Q()

	# 		comb_fil = fil_lenght & fil_width & fil_base & fil_color

	# 		filted_result = result.filter(comb_fil)
	# else:
	# 	bed = BedForm()


# Image(submit) Result

	# bed = None
	# filtered_image = None

	# if request.method == 'POST':
		# bed = BedForm(request.POST)
		# if bed.is_valid():
		# 	lenght = bed.cleaned_data['lenght'] 
		# 	width = bed.cleaned_data['width']
		# 	base = bed.cleaned_data['base']
		# 	color = bed.cleaned_data['color']
	# 		try:
	# 			filtered_image = Bed.objects.get(
	# 				lenght=lenght,
	# 				width=width,
	# 				base=base,
	# 				color=color
	# 				)
	# 		except Bed.DoesNotExist:
	# 			filtered_image = None
	# 	else:
	# 		form = BedForm()

	# context = {
	# 	'bed': bed,
	# 	# 'filted_result': filted_result,
	# 	'filtered_image': filtered_image,

	# }



	if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
		form = BedForm(request.POST)
		if form.is_valid():
			selected_length = request.POST.get('length')
			selected_width = request.POST.get('width')
			# selected_base = request.POST.get('base')
			# selected_color = request.POST.get('color')

			selected_language = request.POST.get('language', 'en')
			selected_parameters = {}

			parameter_translations = PARAMETER_TRANSLATIONS.get(selected_language, {})

			for param in ['base', 'color']:
				param_translation = parameter_translations.get(param, param)
				selected_parameters[param_translation] = request.POST.get(param)

			beds = Bed.objects.filter(
				length=selected_length,
				width=selected_width,
				**selected_parameters)

			results = []
			for bed in beds:
				results.append({
		    		'length': bed.length,
		    		'width': bed.width,
		    		'base': bed.base,
		    		'color': bed.color,
		    		'images': bed.images.url,
		        })

			return JsonResponse({'beds': results})


	context = {
		'form': BedForm(),
	}

	return render(request, 'mebels/index.html', context)


