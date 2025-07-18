import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Plugin
from .utils import update_plugins, serve_plugins


# VIEWS ############################################################################################
def plugin_list(request: HttpRequest) -> HttpResponse:
    base_url = request.build_absolute_uri('/')
    # Update plugins before rendering the plugin list
    update_plugins()
    plugins = Plugin.objects.all()

    qgis_version = request.GET.get('qgis')
    if qgis_version:
       # Generate XML content based on the qgis_version using serve_plugins function
        xml_content = serve_plugins(qgis_version, base_url)

        # Set Content-Type header to indicate XML response
        return HttpResponse(xml_content, content_type='application/xml') 

    return render(request, 'plugin_list.html', {'plugins': plugins})


def download_plugin(request: HttpRequest, plugin_name: str) -> HttpResponse:
    # Get the plugin object
    plugin = get_object_or_404(Plugin, file_name__contains=plugin_name)
    
    # Construct file path
    _file_name = plugin_name if '.zip' in plugin_name else f'{plugin_name}.zip'
    file_path = os.path.join(settings.PLUGIN_ZIP_UPLOAD_DIR, f'{_file_name}')
    # Check if the plugin file exists
    if not os.path.exists(file_path):
        return HttpResponse(f"{request.path}: The zip-file for plugin '{plugin_name}' does not exist.", status=404)

    # Increment download count if DOWNLOAD_COUNTER is enabled
    if settings.DOWNLOAD_COUNTER:
        plugin.downloads += 1
        plugin.save()

    # Prepare response for file download
    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{plugin_name}.zip"'

    # Read and serve the file
    with open(file_path, 'rb') as file:
        response.write(file.read())

    return response


# Add view function to handle plugin upload
def upload_plugin(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"{request.path} operation not implemented yet.")
    if request.method == 'POST' and request.FILES['plugin_zip']:
        plugin_zip = request.FILES['plugin_zip']
        # Save the uploaded plugin zip file to the designated directory
        fs = FileSystemStorage(location=settings.PLUGIN_ZIP_UPLOAD_DIR)
        filename = fs.save(plugin_zip.name, plugin_zip)
        # Optionally, update the database with the file path or other relevant information
        # For example:
        # Plugin.objects.create(zip_path=filename, ...)
        return redirect('plugin_list')
    return render(request, 'upload_plugin.html')
