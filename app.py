import streamlit as st

st.title("Galery of animals")

if "animals" not in st.session_state:
  st.session_state.animals = []

st.header("Add an animal")
name = st.text_input("Name of the animal: ")
description = st.text_input("Description: ")
image_url = st.text_input(" Image URL")

if st.header("add"):
  if name and description and image_url:
    st.session_state.animals.append({
      "name": name,
      "Description": description,
      "Image": image_url
    })
    st.succes(f"{name} is added!")

else:
  st.warning("Please enter all of the information")


if st.session_state.animals:
  st.header("Delete animal")
  names = []
  for a in st.session_state.animals:
    names.append(a["name"])

remove_name = st.selection("Pick an animal to delete:" , names)

if st.button("Delete"):
  for a in st.session_state.animals:
    if(a["name"] == remove._names:
      st.session_state.animals.remove(a)
      break

st.succes(f"{remove.name} is deleted")


st.header("Galery")
if st.session_state.animals:
  cols=st.columns(3)
  for idx, animal in enumerate (st.session_state.animals):
    with (cols[idx % 3]:
      st.subheader(animal["name"])
      st.image(animal["image"], use_column_width = True)
      st.write(animal["description"])

else:
  st.info("The galery is rmpty")




