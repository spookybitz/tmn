import pastel

pastel.add_style('hg', 'green')
pastel.add_style('hgb', 'green', options=['bold'])
pastel.add_style('hy', 'yellow')
pastel.add_style('hyb', 'yellow', options=['bold'])
pastel.add_style('link', 'yellow', options=['underscore'])
pastel.add_style('und', options=['underscore'])
pastel.add_style('warning', 'yellow')
pastel.add_style('error', 'red')


def newline(number=1):
    """
    Print newlines

    :param number: the number of newlines to print
    :type number: int
    """
    print('\n'*number, end='')


def style(function):
    """
    Print and colorize strings with `pastel`

    :param function: function to decorate
    :type function: function
    :returns: decorated function
    :rtype: function
    """
    def wrapper(*args):
        print(pastel.colorize(function(*args)))
    return wrapper


def style_no_new_line(function):
    """
    Print and colorize strings with `pastel`. Don't add a new line at the end.

    Decorator to print and colorize strings with `pastel`.
    Don't add a new line at the end.

    :param function: function to decorate
    :type function: function
    :returns: decorated function
    :rtype: function
    """
    def wrapper(*args):
        print(pastel.colorize(function(*args)), end='', flush=True)
    return wrapper


@style
def link(msg, url):
    """
    Return a pastel formated string for browser links

    :param msg: message
    :type msg: str
    :param url: website url
    :type url: str
    """
    return '<hg>{msg}</hg> <link>{url}</link>'.format(
        msg=msg,
        url=url
    )


def link_docs(url):
    """
    Custom link message for documentation

    :param url: url to display
    :type url: str
    """
    link('Documentation on running a masternode:', url)


def link_docs_open(url):
    """
    Custom link message for documentation, 'open in browser' version

    :param url: url to display
    :type url: str
    """
    link('Opening documentation:', url)


@style
def title(msg):
    """
    Return a pastel formated title string

    :param msg: title message
    :type msg: str
    :returns: subtitle formated
    :rtype: str
    """
    return '<hg>{msg}</hg>\n'.format(
        msg=msg
    )


def title_start_masternode():
    """
    Title when starting a masternode
    """
    title('Starting your masternode!')


def title_stop_masternode():
    """
    Title when stopping a masternode
    """
    title('Stopping your masternode!')


@style
def subtitle(msg):
    """
    Return a pastel formated subtitle string

    :param msg: subtitle message
    :type msg: str
    :returns: subtitle formated
    :rtype: str
    """
    return '<und>{msg}</und>\n'.format(
        msg=msg
    )


def subtitle_create_volumes():
    """
    Subtitle when creating volumes
    """
    subtitle('Volumes')


def subtitle_create_networks():
    """
    Subtitle when creating networks
    """
    subtitle('Networks')


def subtitle_create_containers():
    """
    Subtitle when creating containers
    """
    subtitle('Containers')


@style_no_new_line
def step(msg, indent=1):
    """
    Return a pastel formated step with indentation.
    One indent is two spaces.

    :param msg: step message
    :type msg: str
    :param indent: number of idents
    :type indent: int
    :returns: `msg` formated
    :rtype: str
    """
    step = '  '*indent + '- {msg}... '.format(
        msg=msg
    )
    return step


def step_create_masternode_volume(volume):
    """
    Custom step message for docker volumes creation
    """
    step('Creating <hy>{volume}</hy>'.format(
        volume=volume
    ))


def step_create_masternode_network(network):
    """
    Custom step message for docker networks creatin
    """
    step('Creating <hy>{network}</hy>'.format(
        network=network
    ))


def step_create_masternode_container(container):
    """
    Custom step message for docker container creation
    """
    step('Creating <hy>{container}</hy>'.format(
        container=container
    ))


def step_start_masternode_container(container):
    """
    Custom step message for docker container starting
    """
    step('Starting <hy>{container}</hy>'.format(
        container=container
    ))


def step_stop_masternode_container(container):
    """
    Custom step message for docker container stopping
    """
    step('Stopping <hy>{container}</hy>'.format(
        container=container
    ))


@style
def step_close(msg, color='green'):
    """
    Return a pastel formated end of step

    :param msg: task status of the step
    :type msg: str
    :returns: `msg` formated
    :rtype: str
    """
    return '<fg={color}>{msg}</>'.format(
        msg=msg,
        color=color
    )


def step_close_created():
    """
    Custom 'created' closing step message
    """
    step_close('created')


# def step_close_exist():
#     """
#     Custom 'exist' closing step message
#     """
#     step_close('exist')


def step_close_exists():
    """
    Custom 'exists' closing step message
    """
    step_close('exists')


def step_close_status(status):
    """
    Custom 'status' closing step message
    """
    step_close(status)


# @style
# def warning(msg):
#     """
#     Return a pastel formated string for warnings
#
#     :param msg: warning message
#     :type msg: str
#     """
#     return '<warning>! warning:</warning> {msg}\n'.format(
#         msg=msg
#     )


@style
def error(msg):
    """
    Return a pastel formated string for errors

    :param msg: error message
    :type msg: str
    :returns: `msg` formated
    :rtype: str
    """
    return '<error>! error:</error> {msg}\n'.format(
        msg=msg
    )


def error_docker():
    """
    Custom error when docker is not accessible
    """
    error('could not access the docker daemon')


def error_docker_api():
    """
    Custom error when docker is not accessible
    """
    error('something went wrong while doing stuff with docker')


def error_config():
    """
    Custom error when configuration is not accessible or when you can't
    create it
    """
    error('could not access or create configuration file')


# def error_docker_state(name, state):
#     """
#     Custom error when configuration is not accessible or when you can't
#     create it
#     """
#     error(
#         'your container <hy>{name}</hy>'.format(
#             name=name
#         ),
#         'was in unexpected state <hy>{state}</hy>'.format(
#             state=state
#         )
#     )