import sys
import json
import geopandas as gpd
import os

def dissolve_geometries(input_shapefile, dissolve_field=None):
    try:
        # Read the shapefile
        gdf = gpd.read_file(input_shapefile)

        # Handle 'None' as a string from CWL
        if dissolve_field == "None":
            dissolve_field = None

        # Perform dissolve operation
        if dissolve_field:
            gdf_dissolved = gdf.dissolve(by=dissolve_field)
        else:
            gdf_dissolved = gdf.dissolve()

        # Construct output file names in the current directory
        output_geojson = os.path.join(os.getcwd(), "dissolved_shp.geojson")

        # Save the dissolved GeoJSON
        gdf_dissolved.to_file(output_geojson, driver='GeoJSON')
        return gdf_dissolved, output_geojson  # Return the dissolved GeoDataFrame and output path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None  # Ensure two values are returned even in case of an error

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dissolve_shp.py <input_shapefile> [<dissolve_field>]")
        sys.exit(1)

    input_shapefile = sys.argv[1]
    dissolve_field = sys.argv[2] if len(sys.argv) > 2 else "None"

    results, output_geojson = dissolve_geometries(input_shapefile, dissolve_field)

    if results is not None:
        print(f"Results successfully saved as {output_geojson}")
    else:
        print(json.dumps({"error": "Dissolve operation failed"}))
