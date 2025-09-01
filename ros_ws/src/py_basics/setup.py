from setuptools import setup

package_name = 'py_basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dev',
    maintainer_email='dev@example.com',
    description='Basic ROS 2 talker example',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker=py_basics.talker:main',
        ],
    },
)
