from astropy_helpers.commands.test import AstropyTest
import os

class PlasmaPyTest(AstropyTest):
    def _generate_coverage_commands(self):
        """
        This method creates the post and pre commands if coverage is to be
        generated
        """
        if self.parallel != 0:
            raise ValueError(
                "--coverage can not be used with --parallel")

        try:
            import coverage  # pylint: disable=W0611
        except ImportError:
            raise ImportError(
                "--coverage requires that the coverage package is "
                "installed.")

        # Don't use get_pkg_data_filename here, because it
        # requires importing astropy.config and thus screwing
        # up coverage results for those packages.
        #coveragerc = os.path.join(
        #    self.testing_path, self.package_name.replace('.', '/'),
        #    'tests', 'coveragerc')
        coveragerc = '.coveragerc'

        with open(coveragerc, 'r') as fd:
            coveragerc_content = fd.read()

        coveragerc_content = coveragerc_content.replace(
            "{packagename}", self.package_name.replace('.', '/'))
        tmp_coveragerc = os.path.join(self.tmp_dir, 'coveragerc')
        with open(tmp_coveragerc, 'wb') as tmp:
            tmp.write(coveragerc_content.encode('utf-8'))

        cmd_pre = (
            'import coverage; '
            'cov = coverage.coverage(data_file="{0}", config_file="{1}"); '
            'cov.start();'.format(
                os.path.abspath(".coverage"), tmp_coveragerc))
        cmd_post = (
            'cov.stop(); '
            'from astropy.tests.helper import _save_coverage; '
            '_save_coverage(cov, result, "{0}", "{1}");'.format(
                os.path.abspath('.'), self.testing_path))

        return cmd_pre, cmd_post
