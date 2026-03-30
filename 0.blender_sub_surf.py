# Warning: This script will cause Blender to crash.
# However, I'm not proficient in Blender, so I don't know how to fix it.
# You may need to run it multiple times to complete the processing of all the meshes.
import os

import bpy


MASS_HUMANS_PATH = "C:/Users/admin/Documents/makehuman/v1py3/exports"
human_files = [f for f in os.listdir(MASS_HUMANS_PATH) if f.endswith(".obj")]
EXPORT_PATH = "E:/mass_humans"
print(f"Found {len(human_files)} human models in {MASS_HUMANS_PATH}.")

for i in range(len(human_files)):
    output_file = os.path.join(EXPORT_PATH, f"human_{i}.obj")
    if os.path.exists(output_file):
        print(f"Skipping already processed human model {i+1}")
        continue
    print(f"processing human model {i+1}/{len(human_files)}. {human_files[i]}")
    bpy.ops.object.select_all(action="DESELECT")
    human_file = os.path.join(MASS_HUMANS_PATH, human_files[i])
    bpy.ops.wm.obj_import(filepath=human_file)
    imported_objs = bpy.context.selected_objects
    if not imported_objs:
        print(f"Failed to import {human_file}. Skipping.")
        continue
    human_obj = imported_objs[0]
    human_obj.scale = (0.1, 0.1, 0.1)
    human_obj.name = f"human_{i}"
    human_mod = human_obj.modifiers.new(name=f"human_mod", type="SUBSURF")
    human_mod.levels = 1
    human_mod.render_levels = 1

    for slot_index, slot in enumerate(human_obj.material_slots):
        mat = slot.material
        if slot_index == 0:
            target_alpha = 1.0
        elif slot_index == 1:
            target_alpha = 0.999
        nodes = mat.node_tree.nodes
        bsdf_node = None
        for node in nodes:
            if node.type == "BSDF_PRINCIPLED":
                bsdf_node = node
                break
        bsdf_node.inputs["Alpha"].default_value = target_alpha
    bpy.context.view_layer.objects.active = human_obj
    bpy.ops.object.modifier_apply(modifier=human_mod.name)
    bpy.ops.wm.obj_export(filepath=output_file, export_selected_objects=True)
    bpy.data.objects.remove(human_obj, do_unlink=True)
