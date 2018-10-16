from dateutil.parser import parse as timeparser
import yippi

class Set(object):
    def __init__(self, object):
        self.object = object.find("post-set")
        self._description = None
        self._id = None
        self._name = None
        self._post_count = None
        self._public = None
        self._shortname = None
        self._updated_at = None
        self._user_id = None
        self._posts = []

    @property
    def description(self):
        if self.object.description:
            self._description = self.object.description.text
        return self._description

    @property
    def id(self):
        if self.object.id:
            self._id = int(self.object.id.text)
        return self._id

    @property
    def name(self):
        if self.object.name:
            self._name = self.object.find("name").text
        return self._name

    @property
    def post_count(self):
        if self.object.post_count:
            self._post_count = int(self.object.find("post-count").text)
        return self._post_count

    @property
    def public(self):
        if self.object.public:
            self._public = bool(self.object.public.text)
        return self._public

    @property
    def shortname(self):
        if self.object.shortname:
            self._shortname = self.object.shortname.text
        return self._shortname

    @property
    def updated_at(self):
        if self.object.updated_at:
            self._updated_at = timeparser(self.object.find("updated_at").text)
        return self._updated_at

    @property
    def user_id(self):
        if self.object.user_id:
            self._user_id = int(self.object.find("user-id").text)
        return self._user_id

    @property
    def posts(self):
        if self.object.findAll("post"):
            for post in self.object.findAll("post"):
                self._posts.append(Submission(post))
        return self._posts

class Submission(object):
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

    @property
    def description(self):
        if self.object.description:
            self._description = self.object.description.text
        return self._description

    @property
    def id(self):
        if self.object.id:
            self._id = int(self.object.id.text)
        return self._id

    @property
    def tags(self):
        if self.object.tags:
            self._tags = self.object.tags.text.split(' ')
        return self._tags

    @property
    def locked_tags(self):
        if self.object.locked_tags:
            self._locked_tags = bool(self.object.locked_tags.attrs['nil'])
        return self._locked_tags

    @property
    def created_at(self):
        if self.object.created_at:
            self._created_at = timeparser(self.object.created_at.text)
        return self._created_at

    @property
    def creator_id(self):
        if self.object.creator_id:
            self._creator_id = int(self.object.creator_id.text)
        return self._creator_id

    @property
    def author(self):
        if self.object.author:
            self._author = self.object.author.text
        return self._author

    @property
    def change(self):
        if self.object.change:
            self._change = int(self.object.change.text)
        return self._change

    @property
    def source(self):
        if self.object.source:
            self._source = self.object.source.text
        return self._source

    @property
    def score(self):
        if self.object.score:
            self._score = int(self.object.score.text)
        return self._score

    @property
    def fav_count(self):
        if self.object.fav_count:
            self._fav_count = int(self.object.fav_count.text)
        return self._fav_count

    @property
    def md5(self):
        if self.object.md5:
            self._md5 = self.object.md5.text
        return self._md5

    @property
    def file_size(self):
        if self.object.file_size:
            self._file_size = int(self.object.file_size.text)
        return self._file_size

    @property
    def file_url(self):
        if self.object.file_url:
            self._file_url = self.object.file_url.text
        return self._file_url

    @property
    def file_ext(self):
        if self.object.file_ext:
            self._file_ext = self.object.file_ext.text
        return self._file_ext

    @property
    def preview_url(self):
        if self.object.preview_url:
            self._preview_url = self.object.preview_url.text
        return self._preview_url

    @property
    def preview_width(self):
        if self.object.preview_width:
            self._preview_width = int(self.object.preview_width.text)
        return self._preview_width

    @property
    def preview_height(self):
        if self.object.preview_height:
            self._preview_height = int(self.object.preview_height.text)
        return self._preview_height

    @property
    def sample_url(self):
        if self.object.sample_url:
            self._sample_url = self.object.sample_url.text
        return self._sample_url

    @property
    def sample_width(self):
        if self.object.sample_width:
            self._sample_width = int(self.object.sample_width.text)
        return self._sample_width

    @property
    def sample_height(self):
        if self.object.sample_height:
            self._sample_height = int(self.object.sample_height.text)
        return self._sample_height

    @property
    def rating(self):
        if self.object.rating:
            self._rating = self.object.rating.text
        return self._rating

    @property
    def status(self):
        if self.object.status:
            self._status = self.object.status.text
        return self._status

    @property
    def width(self):
        if self.object.width:
            self._width = int(self.object.width.text)
        return self._width

    @property
    def height(self):
        if self.object.height:
            self._height = int(self.object.height.text)
        return self._height

    @property
    def has_comments(self):
        if self.object.has_comments:
            self._has_comments = bool(self.object.has_comments.text)
        return self._has_comments

    @property
    def has_notes(self):
        if self.object.has_notes:
            self._has_notes = bool(self.object.has_notes.text)
        return self._has_notes

    @property
    def has_children(self):
        if self.object.has_children:
            self._has_children = bool(self.object.has_children.text)
        return self._has_children

    @property
    def children(self):
        if self.object.children.text:
            self._children = self.object.children.text
            splitted = self._children.split(',')
            self._children = []
            for child in splitted:
                self._children.append(yippi.post(child))
        return self._children

    @property
    def parent_id(self):
        if self.object.parent_id:
            self._parent_id = yippi.post(self.object.parent_id.text)
        return self._parent_id

    @property
    def artist(self):
        if self.object.artist:
            self._artist = self.object.artist.artist.text
        return self._artist

    @property
    def sources(self):
        if self.object.sources:
            for source in self.object.sources.findAll("source"):
                self._sources.append(source.text)
        return self._sources
