# HELPERS ##########################################################################################
import os
import zipfile
from datetime import datetime
import xml.etree.ElementTree as ET
from django.conf import settings
from django.urls import reverse
from .models import Plugin


def update_plugins():
    def handle_plugin_file(plugin_file):
        plugin_path = os.path.join(settings.PLUGIN_ZIP_UPLOAD_DIR, plugin_file)
        if os.path.isfile(plugin_path) and plugin_file.endswith('.zip'):
            metadata = parse_metadata(plugin_path)
            if metadata:
                process_plugin_metadata(metadata, plugin_file)

    def process_plugin_metadata(metadata, plugin_file):
        existing_plugin = Plugin.objects.filter(name=metadata['name']).first()
        if not existing_plugin:
            create_new_plugin(metadata, plugin_file)
        else:
            existing_version = existing_plugin.version
            new_version = metadata['version']
            if compare_versions(new_version, existing_version) > 0:
                update_existing_plugin(existing_plugin, metadata)

    for plugin_file in os.listdir(settings.PLUGIN_ZIP_UPLOAD_DIR):
        handle_plugin_file(plugin_file)


def parse_metadata(zip_file):
    # metadata_file = 'metadata.txt'
    # extract plugin name from zip file (last element of the path)
    plugin_name = os.path.basename(zip_file).split('\\')[-1].split('.')[0]
    metadata_file = plugin_name + '/metadata.txt' 
    # print(metadata_file)

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:

        # print(zip_ref.namelist())
        if metadata_file in zip_ref.namelist():

            with zip_ref.open(metadata_file) as file:
                # print(file)
                data = file.read().decode('utf-8')
                # print(data)
                metadata = {}
                
                for line in data.splitlines():
                    try:
                        key, value = line.split('=', 1)
                        metadata[key.strip()] = value.strip()
                    except ValueError:
                        # not a key-value pair
                        pass
                return metadata
    return None


def update_existing_plugin(existing_plugin, metadata):
    existing_plugin.version = metadata.get('version', existing_plugin.version)
    existing_plugin.description = metadata.get('description', existing_plugin.description)
    existing_plugin.about = metadata.get('about', existing_plugin.about)
    existing_plugin.qgis_minimum_version = metadata.get('qgisMinimumVersion', existing_plugin.qgis_minimum_version)
    existing_plugin.qgis_maximum_version = metadata.get('qgisMaximumVersion', existing_plugin.qgis_maximum_version)
    existing_plugin.homepage = metadata.get('homepage', existing_plugin.homepage)
    existing_plugin.file_name = existing_plugin.file_name or os.path.basename(existing_plugin.file_name)
    existing_plugin.download_url = metadata.get('downloadUrl', existing_plugin.download_url)
    existing_plugin.uploaded_by = metadata.get('author', existing_plugin.uploaded_by)
    existing_plugin.create_date = datetime.now()
    existing_plugin.update_date = datetime.now()
    existing_plugin.experimental = metadata.get('experimental', False)
    existing_plugin.deprecated = metadata.get('deprecated', False)
    existing_plugin.tracker = metadata.get('tracker', '')
    existing_plugin.repository = metadata.get('repository', '')
    existing_plugin.tags = metadata.get('tags', '')
    existing_plugin.external_dependencies = metadata.get('externalDependencies', '')
    existing_plugin.server = metadata.get('server', False)
    existing_plugin.downloads = metadata.get('downloads', 0)
    existing_plugin.save()


def create_new_plugin(metadata, file_name):
    Plugin.objects.create(
        name=metadata.get('name', ''),
        version=metadata.get('version', '0.0.0'),
        description=metadata.get('description', ''),
        about=metadata.get('about', ''),
        qgis_minimum_version=metadata.get('qgisMinimumVersion', '3.00'),
        qgis_maximum_version=metadata.get('qgisMaximumVersion', '3.98'),
        homepage=metadata.get('homepage', ''),
        file_name=file_name,
        download_url=metadata.get('download_url', ''),
        uploaded_by=metadata.get('uploaded_by', ''),
        create_date=datetime.now(),
        update_date=datetime.now(),
        experimental=metadata.get('experimental', False),
        deprecated=metadata.get('deprecated', False),
        tracker=metadata.get('tracker', ''),
        repository=metadata.get('repository', ''),
        tags=metadata.get('tags', ''),
        external_dependencies=metadata.get('external_dependencies', ''),
        server=metadata.get('server', False),
        downloads=metadata.get('downloads', 0)
    )


def compare_versions(version1, version2):
    # Implement your version comparison logic here
    # For simplicity, assume version strings are in x.y.z format
    v1 = [int(x) for x in version1.split('.')]
    v2 = [int(x) for x in version2.split('.')]
    
    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1
    else:
        return 0


def process_plugin(file, filedir, base_url, qgis_version, root):
    try:
        filepath = os.path.join(filedir, file)
        metadata = parse_metadata(filepath)
        if metadata:
            minversion = metadata.get('qgisMinimumVersion', settings.DEFAULT_MIN_QGIS_VERSION)
            maxversion = metadata.get('qgisMaximumVersion', minversion[:1] + ".98" if minversion[1:4] == ".99" else minversion[:1] + ".99")
            if qgis_version == "" or (qgis_version >= minversion and qgis_version <= maxversion):
                full_download_url = create_download_url(base_url, file)
                plugin_elem = create_plugin_element(metadata, file, full_download_url, minversion, maxversion)
                root.append(plugin_elem)
    except Exception as e:
        print(f"Error processing plugin {file}: {e}")


def create_download_url(base_url, file):
    download_url = reverse('qgs_plugins:download', args=[file.split('.')[0]])
    return f'{base_url}{download_url[1:]}'


def create_plugin_element(metadata, file, full_download_url, minversion, maxversion):
    plugin_elem = ET.Element(
        "pyqgis_plugin",
        name=metadata.get('name', ''),
        version=metadata.get('version', ''),
        plugin_id=str(abs(hash(metadata.get('name', ''))))
    )
    description_elem = ET.SubElement(plugin_elem, "description")
    description_elem.text = metadata.get('description', '')
    about_elem = ET.SubElement(plugin_elem, "about")
    about_elem.text = metadata.get('about', '')
    version_elem = ET.SubElement(plugin_elem, "version")
    version_elem.text = metadata.get('version', '')
    min_version_elem = ET.SubElement(plugin_elem, "qgis_minimum_version")
    min_version_elem.text = minversion
    max_version_elem = ET.SubElement(plugin_elem, "qgis_maximum_version")
    max_version_elem.text = maxversion
    homepage_elem = ET.SubElement(plugin_elem, "homepage")
    homepage_elem.text = metadata.get('homepage', '')
    file_name_elem = ET.SubElement(plugin_elem, "file_name")
    file_name_elem.text = file
    icon_elem = ET.SubElement(plugin_elem, "icon")
    icon_elem.text = metadata.get('icon', '')
    author_name_elem = ET.SubElement(plugin_elem, "author_name")
    author_name_elem.text = metadata.get('author_name', '')
    download_url_elem = ET.SubElement(plugin_elem, "download_url")
    download_url_elem.text = full_download_url
    uploaded_by_elem = ET.SubElement(plugin_elem, "uploaded_by")
    uploaded_by_elem.text = metadata.get('uploaded_by', '')
    create_date_elem = ET.SubElement(plugin_elem, "create_date")
    create_date_elem.text = metadata.get('create_date', '')
    update_date_elem = ET.SubElement(plugin_elem, "update_date")
    update_date_elem.text = metadata.get('update_date', '')
    experimental_elem = ET.SubElement(plugin_elem, "experimental")
    experimental_elem.text = metadata.get('experimental', '')
    deprecated_elem = ET.SubElement(plugin_elem, "deprecated")
    deprecated_elem.text = metadata.get('deprecated', '')
    tracker_elem = ET.SubElement(plugin_elem, "tracker")
    tracker_elem.text = metadata.get('tracker', '')
    repository_elem = ET.SubElement(plugin_elem, "repository")
    repository_elem.text = metadata.get('repository', '')
    tags_elem = ET.SubElement(plugin_elem, "tags")
    tags_elem.text = metadata.get('tags', '')
    downloads_elem = ET.SubElement(plugin_elem, "downloads")
    downloads_elem.text = metadata.get('downloads', '')
    average_vote_elem = ET.SubElement(plugin_elem, "average_vote")
    average_vote_elem.text = metadata.get('average_vote', '')
    rating_votes_elem = ET.SubElement(plugin_elem, "rating_votes")
    rating_votes_elem.text = metadata.get('rating_votes', '')
    external_dependencies_elem = ET.SubElement(plugin_elem, "external_dependencies")
    external_dependencies_elem.text = metadata.get('external_dependencies', '')
    server_elem = ET.SubElement(plugin_elem, "server")
    server_elem.text = metadata.get('server', '')
    return plugin_elem

def serve_plugins(qgis_version: int, base_url: str):
    filedir = settings.PLUGIN_ZIP_UPLOAD_DIR
    root = ET.Element("plugins")
    allfiles = os.listdir(filedir)
    allfiles.sort(key=str.lower)
    
    for file in allfiles:
        if file.endswith(".zip"):
            process_plugin(file, filedir, base_url, qgis_version, root)
                
    xml_str = ET.tostring(root, encoding='utf-8', method='xml').decode()
    print(xml_str)
    return xml_str
