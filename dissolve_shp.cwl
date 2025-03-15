cwlVersion: v1.2
class: CommandLineTool
hints:
  DockerRequirement:
    dockerPull: eforoutan/dissolve_shp:latest
  NetworkAccess:
    networkAccess: true

inputs:
  input_shapefile:
    type: Directory
    inputBinding:
      position: 1

  dissolve_field:
    type: string
    default: "None"
    inputBinding:
      position: 2

outputs:
  Dissolved_GeoJSON:
    type: File  
    outputBinding:
      glob: "dissolved_shp.geojson"