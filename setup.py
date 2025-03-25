from setuptools import setup, find_packages

setup(
    name="albutils",  # Nombre del paquete
    version="0.2",
    packages=find_packages(),
    install_requires=[],  # Dependencias (puedes agregar más si las necesitas)
    author="Diego García",
    author_email="dgarcia@albentia.com",
    description="Paquete albentiano que incluye clases simples para la creación de entornos de producción para placas externas.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    #url="https://github.com/tu_usuario/mi_paquete",  # URL de tu repo (opcional)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

