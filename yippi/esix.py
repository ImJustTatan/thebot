import urllib.request, json, datetime, yippi.object, yippi.helper, yippi.xml.object

headers = {
    'User-Agent': 'Yippi/1.0 (by Error- on e621)'
}

class search:
    """
    Main search feature, this doesn't have any parameter to process."""
    def post(self, tags : list, rating="e", limit=50, page=1, **kwargs):
        """
        Searches e621 submission
    
        :Parameters:
    
        tags : [:class:`list`]
            The tags that will be given to and processed by e621
        rating : [Optional :class:`str`]
            Rating that will be used to search, refer to `e621 cheatseet`_ for more information, defaults to "e"
        limit : [Optional :class:`int`]
            Limit total results from e621 API, defaults to 50
        page : [Optional :class:`int`]
            Scroll through the page given, defaults to page 1
    
        Every kwargs will be processed like what `e621 cheatseet` said
    
        .. _e621 cheatseet: https://e621.net/help/show/cheatsheet
    
        :Return:
    
        This command will return list of :class:`yippi.object.Submission` object"""
        extratags = []
        for kw in list(kwargs.items()):
            kw =':'.join(kw)
            extratags.append(kw)
        apiurl = 'https://e621.net/post/index.json?tags=%s+rating:%s+%s&limit=%s&page=%s' \
            % ('+'.join(tags), rating, '+'.join(extratags), limit, page)
        results = yippi.helper.getAPI(apiurl)
        objects = []
        for obj in results:
            esixobject = yippi.object.Submission(obj)
            objects.append(esixobject)
        return objects

    def artist(self, name : str, limit=10, order="name", page=1):
        """
        Searches e621 artist info
        :Parameters:
        name : [:class:`str`]
            Artist name that will be given as query to e621 API
        limit : [:class:`int`]
            Limit total results from e621 API, defaults to 50
        order : [:class:`str`]
            Order the result based on "date" or "name", defaults to "name"
        page : [:class:`int`]
             Scroll through the page given, defaults to page 1
        :Returns:
        :class:`yippi.object.Artist` object of the artist"""
        apiurl = 'https://e621.net/artist/index.json?name=%s&limit=%s&order=%s&page=%s' \
            % (name, limit, order, page)
        results = yippi.helper.getAPI(apiurl)
        objects = []
        for obj in results:
            esixobject = yippi.object.Artist(obj)
            objects.append(esixobject)
        return objects

    def user(self, *, id="", name="", level=-1, order="name"):
        """
        Searches user at e621
        :Parameters:
        id : [:class:`int`]
            The user ID to search
        name : [:class:`str`]
            Text query matching part or all of a user's name
        level : [:class:`int` or :class:`yippi.object.UserLevel]
            Permission level to search
        order : [:class:`str`]
            Sort of order, defaults to `name`
        :Returns:
        :class:`yippi.object.User` object"""
        if not id and not name:
            print("Please specify either id or name!")
            return
        if isinstance(level, yippi.object.UserLevel):
            level = level.value
        apiurl = "https://e621.net/user/index.json?id=%s&name=%s&level=%s&order=%s" % (id, name, level, order)
        result = yippi.helper.getAPI(apiurl)
        objects = []
        for obj in result:
            esixobject = yippi.object.User(obj)
            objects.append(esixobject)
        return objects

    def pool(self, name, page=1):
        apiurl = 'https://e621.net/pool/index.json?query=%s&page=%s' \
            % (name, page)
        results = yippi.helper.getAPI(apiurl)
        objects = []
        for obj in results:
            apiurl = 'https://e621.net/pool/show.json?id=%s' \
                % (obj['id'])
            result = yippi.helper.getAPI(apiurl)
            esixobject = yippi.object.Pool(result)
            objects.append(esixobject)
        return objects

    def set(self, *, page=1, user=None, maintainer=None, post=None, id=None):
        if id:
            apiurl = 'https://e621.net/set/show.xml?id=%s' \
                % (id)  
            result = yippi.helper.getxmlAPI(apiurl)
            return yippi.xml.object.Set(result)
        apiurl = 'https://e621.net/set/index.xml?page=%s&maintainer_id=%s&user_id=%s&post_id=%s' \
            % (page, user, maintainer, post)
        results = yippi.helper.getxmlAPI(apiurl)
        sets = []
        for set in results.findAll("set"):
            apiurl = 'https://e621.net/set/show.xml?id=%s' \
                % (set.id)
            result = yippi.helper.getxmlAPI(apiurl)
            sets.append(yippi.xml.object.Set(result))
        return sets

def post(id : int):
    """
    Opens a e621 post
    :Parameters:
    id : :class:`int`
        The post ID of a submission
    :Return:
    :class:`yippi.object.Submission` object of the post"""
    apiurl = "https://e621.net/post/show.json?id=%s" % (id)
    result = yippi.helper.getAPI(apiurl)
    return yippi.object.Submission(result)

def get_level(lvl : str):
    """
    Get the :class:`yippi.object.UserLevel` object of requested UserLevel"""
    Level = {
        'Everyone': -1,
        'Unactivated': 0,
        'Blocked': 10,
        'Member': 20,
        'Privileged': 30,
        'Staff': 34,
        'Janitor': 35,
        'Mod': 40,
        'Admin': 50
    }

    lvl = Level[lvl]
    return yippi.object.UserLevel(lvl)

def get_tag(tag : str):
    return yippi.object.Tag(yippi.helper.getTagsInfo(tag))
