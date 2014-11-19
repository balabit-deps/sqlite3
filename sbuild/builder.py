from AutotoolsBuilder import AutotoolsBuilder
import Utils

class SqliteBuilder(AutotoolsBuilder):
    def bootstrap(self):
        result = super(SqliteBuilder, self).bootstrap() and super(SqliteBuilder, self).configure()
        self.make("sqlite3.h")
        Utils.run_command("mv '%s/sqlite3.h' '%s/sqlite3.h-bb'"%(self.build_dir, self.build_dir))
        self.make("distclean")
        return result

    def configure(self, configure_opts = None):
        result = super(SqliteBuilder, self).configure(configure_opts)
        Utils.run_command("cp '%s/sqlite3.h-bb' '%s/sqlite3.h'"%(self.build_dir, self.build_dir))
        Utils.run_command("touch '%s/sqlite3.h'"%(self.build_dir))
        return result
        

def get_builder():
    return SqliteBuilder(get_default_config_opts())

def get_default_config_opts():
    try:
        import configure_opts
    except ImportError:
        return None
    else:
        return configure_opts.default_opts
