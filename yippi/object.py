import datetime, yippi, urllib.request, yippi.helper

class Submission(object):
    """
    A representation of e621 submission post object
    :Parameters:
    object : [:class:`dict`]
        A JSON or dict of the submission given from e621 API, this should be a valid JSON or everything will broke
    :Functions:
    .. function:: download(file_name)
        Downloads the submission's file
    :Attributes:
    
    id : :class:`int`
        The post ID of the submission
    tags : :class:`list`
        Tags of the submission, splitted with every space
    locked_tags : :class:`bool`
        Check if the tags are locked for edit
    description : :class:`str`
        Description of the submission, if no description is given, this will be a `None` object
    created_at : :class:`str`
        Date of the submission is posted
    creator_id : :class:`int`
        The creator's user ID
    author : :class:`str`
        Author of the submission
    change : :class:`int`
        This thing is still unknown, e621 doesn't give any info about this
    source : :class:`str`
        Source of the submission, taken from :function:sources and took the very first value of it
    sources : :class:`list`
        List of the source of the submission
    score : :class:`int`
        The score of the submission
    fav_count : :class:`int`
        Total favorites of the submission
    md5 : :class:`str`
        MD5 checksum of the submission file
    file_size : :class:`int`
        Size of the submission file in bytes
    file_url : :class:`str`
        Submission file URL
    file_ext : :class:`str`
        Submission file extension
    rating : :class:`str`
        Rating of the submission, refer to `e621 cheatseet`_ for more information
    status : :class:`str`
        Submission status, one of: active, flagged, pending, deleted
    width : :class:`int`
        The width of the file in pixel
    height : :class:`int`
        Same as :function:width but with height
    has_comments : :class:`bool`
        Check if the submission has comments or not
    has_children : :class:`bool`
        Check if the submission has children post or not
    children : :class:`list`
        The child post of the submission, if there's none, it will return `None` object
    parent : :class:`int`
        Parent post of the submission, if there's none, it will return `None` object
    artist : :class:`list`
        The artist who draw the submission, of course.
        
    .. _e621 cheatseet: https://e621.net/help/show/cheatsheet"""
    
    def __init__(self, object):
        self.object = object
        self._id = None
        self._tags = None
        self._locked_tags = None
        self._description = None
        self._created_at = None
        self._creator_id = None
        self._author = None
        self._change = None
        self._source = None
        self._sources = None
        self._score = None
        self._fav_count = None
        self._md5 = None
        self._file_size = None
        self._file_url = None
        self._file_ext = None
        self._rating = None
        self._status = None
        self._width = None
        self._height = None
        self._has_comments = None
        self._has_notes = None
        self._has_children = None
        self._children = None
        self._parent = None
        self._artist = None

    def __repr__(self):
        return str(self.object)

    @property
    def created_at(self):
        created_timestamp = self.object['created_at']['s']
        self._created_at = datetime.datetime.fromtimestamp(int(created_timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        return self._created_at

    @property
    def id(self):
        if self.object['id']:
            self._id = self.object['id']
        return self._id

    @property
    def tags(self):
        if self.object['tags']:
            self._tags = self.object['tags'].split(" ")
        return self._tags

    @property
    def locked_tags(self):
        if self.object['locked_tags']:
            self._locked_tags = self.object['locked_tags']
        return self._locked_tags

    @property
    def description(self):
        if self.object['description']:
            self._description = self.object['description']
        return self._description

    @property
    def creator_id(self):
        if self.object['creator_id']:
            self._creator_id = self.object['creator_id']
        return self._creator_id

    @property
    def author(self):
        if self.object['author']:
            self._author = self.object['author']
        return self._author

    @property
    def change(self):
        if self.object['change']:
            self._change = self.object['change']
        return self._change

    @property
    def source(self):
        if self.object['source']:
            self._source = self.object['source']
        return self._source

    @property
    def sources(self):
        if self.object['sources']:
            self._sources = self.object['sources']
        return self._sources

    @property
    def score(self):
        if self.object['score']:
            self._score = self.object['score']
        return self._score

    @property
    def fav_count(self):
        if self.object['fav_count']:
            self._fav_count = self.object['fav_count']
        return self._fav_count

    @property
    def md5(self):
        if self.object['md5']:
            self._md5 = self.object['md5']
        return self._md5

    @property
    def file_size(self):
        if self.object['file_size']:
            self._file_size = self.object['file_size']
        return self._file_size

    @property
    def file_url(self):
        if self.object['file_url']:
            self._file_url = self.object['file_url']
        return self._file_url

    @property
    def file_ext(self):
        if self.object['file_ext']:
            self._file_ext = self.object['file_ext']
        return self._file_ext

    @property
    def rating(self):
        if self.object['rating']:
            self._rating = self.object['rating']
        return self._rating

    @property
    def status(self):
        if self.object['status']:
            self._status = self.object['status']
        return self._status

    @property
    def width(self):
        if self.object['width']:
            self._width = self.object['width']
        return self._width

    @property
    def height(self):
        if self.object['height']:
            self._height = self.object['height']
        return self._height

    @property
    def has_comments(self):
        if self.object['has_comments']:
            self._has_comments = self.object['has_comments']
        return self._has_comments

    @property
    def has_notes(self):
        if self.object['has_notes']:
            self._has_notes = self.object['has_notes']
        return self._has_notes

    @property
    def has_children(self):
        if self.object['has_children']:
            self._has_children = self.object['has_children']
        return self._has_children

    @property
    def children(self):
        if self.object['children']:
            self._children = self.object['children']
            splitted = self._children.split(',')
            self._children = []
            for child in splitted:
                self._children.append(yippi.post(child))
        return self._children

    @property
    def parent(self):
        if self.object['parent_id']:
            self._parent = yippi.post(self.object['parent_id'])
        return self._parent

    @property
    def artist(self):
        if self.object['artist']:
            self._artist = self.object['artist']
        return self._artist

    def download(self, file_name):
        with urllib.request.urlopen(self.file_url) as response, open(file_name, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

class Artist(object):
    """
    A representation of e621 artist info
    :Parameters:
    object : [:class:`dict`]
        A JSON or dict of the artist given from e621 API, this should be a valid JSON or everything will broke
    :Attributes:
    id : :class:`int`
        e621 artist ID
    name : :class:`int`
        The artist name, of course
    other_names : :class:`str`
        Artist's alias(es), separared by comma
    group_name : :class:`str`
        The group or circle that this artist is a member of
    is_active : :class:`bool`
         Whether the artist is still active or not"""
    def __init__(self, object):
        self.object = object
        self._id = None
        self._name = None
        self._other_names = None
        self._group_name = None
        self._urls = None
        self._is_active = None
        self._version = None
        self._updater_id = None

    def __repr__(self):
        return str(self.object)

    @property
    def id(self):
        if self.object['id']:
            self._id = self.object['id']
        return self._id

    @property
    def name(self):
        if self.object['name']:
            self._name = self.object['name']
        return self._name

    @property
    def other_names(self):
        if self.object['other_names']:
            self._other_names = self.object['other_names']
        return self._other_names

    @property
    def group_name(self):
        if self.object['group_name']:
            self._group_name = self.object['group_name']
        return self._group_name

    @property
    def urls(self):
        if self.object['urls']:
            self._urls = self.object['urls']
        return self._urls

    @property
    def is_active(self):
        if self.object['is_active']:
            self._is_active = self.object['is_active']
        return self._is_active

    @property
    def version(self):
        if self.object['version']:
            self._version = self.object['version']
        return self._version

    @property
    def updater_id(self):
        if self.object['updater_id']:
            self._updater_id = self.object['updater_id']
        return self._updater_id

class User(object):
    """Representation of user information
    :Parameters:
    object : [:class:`dict`]
        A JSON or dict of the user given from e621 API, this should be a valid JSON or everything will broke
    :Attributes:
    name : :class:`str`
        The username
    id : :class:`int`
        User ID
    level : :class:`UserLevel`
        Level of the user in e621
    created_at : :class:`str`
        Date when user creates the account (YY-MM-DD HH:MM format)
    avatar : :class:`Submission`
        Submission post of the user's avatar
    stats : :class:`UserStats`
        Statistic of user's events at e621
    artist_tags : :class:`list`
        Artist tags associated with the user"""
    def __init__(self, object):
        self.object = object
        self._name = None
        self._id = None
        self._level = None
        self._created_at = None
        self._avatar = None
        self._stats = None
        self._artist_tags = None

    def __repr__(self):
        return str(self.object)

    @property
    def name(self):
        if self.object['name']:
            self._name = self.object['name']
        return self._name

    @property
    def id(self):
        if self.object['id']:
            self._id = self.object['id']
        return self._id

    @property
    def level(self):
        if self.object['level']:
            self._level = self.object['level']
        return UserLevel(self._level)

    @property
    def created_at(self):
        if self.object['created_at']:
            self._created_at = self.object['created_at']
        return self._created_at

    @property
    def avatar(self):
        if self.object['avatar_id']:
            apiurl = "https://e621.net/post/show.json?id=%s" % (id)
            result = yippi.helper.getAPI(apiurl)
            return Submission(result)
        else:
            return self._avatar

    @property
    def stats(self):
        if self.object['stats']:
            self._stats = self.object['stats']
        return UserStats(self._stats)

    @property
    def artist_tags(self):
        if self.object['artist_tags']:
            self._artist_tags = self.object['artist_tags']
        return self._artist_tags

class UserStats(object):
    """
    Representation of user events statistic, all data is in :class:`int`
    :Parameters:
    object : [:class:`dict`]
        A JSON or dict of the submission given from e621 API, this should be a valid JSON or everything will broke
    :Attributes:
    * `post_count`
    * `del_post_count`
    * `edit_count`
    * `favorite_count`
    * `wiki_count`
    * `forum_post_count`
    * `note_count`
    * `comment_count`
    * `blip_count`
    * `set_count`
    * `pool_update_count`
    * `pos_user_records`
    * `neutral_user_records`
    * `neg_user_records`"""
    
    def __init__(self, object):
        self.object = object
        self._post_count = None
        self._del_post_count = None
        self._edit_count = None
        self._favorite_count = None
        self._wiki_count = None
        self._forum_post_count = None
        self._note_count = None
        self._comment_count = None
        self._blip_count = None
        self._set_count = None
        self._pool_update_count = None
        self._pos_user_records = None
        self._neutral_user_records = None
        self._neg_user_records = None

    def __repr__(self):
        return str(self.object)

    @property
    def post_count(self):
        if self.object['post_count']:
            self._post_count = self.object['post_count']
        return self._post_count

    @property
    def del_post_count(self):
        if self.object['del_post_count']:
            self._del_post_count = self.object['del_post_count']
        return self._del_post_count

    @property
    def edit_count(self):
        if self.object['edit_count']:
            self._edit_count = self.object['edit_count']
        return self._edit_count

    @property
    def favorite_count(self):
        if self.object['favorite_count']:
            self._favorite_count = self.object['favorite_count']
        return self._favorite_count

    @property
    def wiki_count(self):
        if self.object['wiki_count']:
            self._wiki_count = self.object['wiki_count']
        return self._wiki_count

    @property
    def forum_post_count(self):
        if self.object['forum_post_count']:
            self._forum_post_count = self.object['forum_post_count']
        return self._forum_post_count

    @property
    def note_count(self):
        if self.object['note_count']:
            self._note_count = self.object['note_count']
        return self._note_count

    @property
    def comment_count(self):
        if self.object['comment_count']:
            self._comment_count = self.object['comment_count']
        return self._comment_count

    @property
    def blip_count(self):
        if self.object['blip_count']:
            self._blip_count = self.object['blip_count']
        return self._blip_count

    @property
    def set_count(self):
        if self.object['set_count']:
            self._set_count = self.object['set_count']
        return self._set_count

    @property
    def pool_update_count(self):
        if self.object['pool_update_count']:
            self._pool_update_count = self.object['pool_update_count']
        return self._pool_update_count

    @property
    def pos_user_records(self):
        if self.object['pos_user_records']:
            self._pos_user_records = self.object['pos_user_records']
        return self._pos_user_records

    @property
    def neutral_user_records(self):
        if self.object['neutral_user_records']:
            self._neutral_user_records = self.object['neutral_user_records']
        return self._neutral_user_records

    @property
    def neg_user_records(self):
        if self.object['neg_user_records']:
            self._neg_user_records = self.object['neg_user_records']
        return self._neg_user_records

class UserLevel(object):
    """
    Representation of level of :class:`User` at e621
    :IDs:
    * 0   Unactivated
    * 10 Blocked
    * 20 Member
    * 30 Privileged
    * 33 Contributor
    * 34 Former Staff
    * 35 Janitor
    * 40 Mod
    * 50 Admin
    :Parameters:
    level : [:class:`int`]
        The level ID of the user
    :Attributes:
    string : :class:`str`
        The permission level string of user
    value : :class:`int`
        Value ID of the object
    """
    def __init__(self, level : int):
        self._levelint = level
        self._Level = {
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

    @property
    def string(self):
        for key, val in self._Level.items():
            if self._levelint == val:
                return key

    @property
    def value(self):
        return self._levelint

class Pool(object):
    def __init__(self, object):
        self.object = object
        self._id = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._user_id = None
        self._name = None
        self._is_active = None
        self._is_locked = None
        self._post_count = None
        self._user_id = None
        self._posts = None

    def __repr__(self):
        return self.name

    @property
    def id(self):
        if self.object['id']:
            self._id = self.object['id']
        return self._id

    @property
    def description(self):
        if self.object['description']:
            self._description = self.object['description']
        return self._description

    @property
    def created_at(self):
        created_timestamp = self.object['created_at']['s']
        self._created_at = datetime.datetime.fromtimestamp(int(created_timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        return self._created_at

    @property
    def updated_at(self):
        if self.object['updated_at']:
            self._updated_at = self.object['updated_at']
        return self._updated_at

    @property
    def user_id(self):
        if self.object['user_id']:
            self._user_id = self.object['user_id']
        return self._user_id

    @property
    def name(self):
        if self.object['name']:
            self._name = self.object['name']
        return self._name

    @property
    def is_active(self):
        if self.object['is_active']:
            self._is_active = self.object['is_active']
        return self._is_active

    @property
    def is_locked(self):
        if self.object['is_locked']:
            self._is_locked = self.object['is_locked']
        return self._is_locked

    @property
    def post_count(self):
        if self.object['post_count']:
            self._post_count = self.object['post_count']
        return self._post_count

    @property
    def posts(self):
        if self.object['posts']:
            self._posts = []
            for post in self.object['posts']:
                object = yippi.object.Submission(post)
                self._posts.append(object)
        return self._posts

class Tag(object):
    def __init__(self, object):
        self.object = object
        self._id = None
        self._name = None
        self._count = None
        self._type = None
        self._type_locked = None
    
    @property
    def id(self):
        if self.object['id']:
            self._id = self.object['id']
        return self._id

    @property
    def name(self):
        if self.object['name']:
            self._name = self.object['name']
        return self._name

    @property
    def count(self):
        if self.object['count']:
            self._count = self.object['count']
        return self._count

    @property
    def type(self):
        if self.object['type']:
            self._type = self.object['type']
        return self._type

    @property
    def type_locked(self):
        if self.object['type_locked']:
            self._type_locked = self.object['type_locked']
        return self._type_locked
