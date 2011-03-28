{
  'conditions': [
    ['OS=="linux"', {
      'target_defaults': {
        'cflags': ['-fPIC', '-g', '-O2',],
        'defines': ['OS_LINUX'],
      },
    },],
    ['OS=="win"', {
      'target_defaults': {
        # 'cflags': ['-fPIC', '-g', '-O2',],
        'defines': ['WIN32', 'OS_WIN', 'NOMINMAX', 'UNICODE', '_UNICODE', '_WIN32_WINNT=0x0501', 'CTEMPLATE_DLL_DECL='],
      },
    },],
  ],
  'targets': [
    {
      'target_name': 'ctemplate',
      'type': 'static_library',
      'msvs_guid': '6FB80D6C-732B-4256-8D39-C2DED7D29434',
#      'include_dirs': ['../src/3rdparty/google-ctemplate/src'],
      'dependencies': [],
      'sources': [
'../src/3rdparty/google-ctemplate/src/base/arena.cc',
'../src/3rdparty/google-ctemplate/src/base/arena.h',
'../src/3rdparty/google-ctemplate/src/base/manual_constructor.h',
'../src/3rdparty/google-ctemplate/src/base/mutex.h',
'../src/3rdparty/google-ctemplate/src/base/small_map.h',
'../src/3rdparty/google-ctemplate/src/base/thread_annotations.h',
#'../src/3rdparty/google-ctemplate/src/config.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/per_expand_data.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/template_annotator.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/template_cache.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/template_dictionary.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/template_dictionary_interface.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/template_emitter.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/template_enums.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/template.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/template_modifiers.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/template_namelist.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/template_pathops.h',
'../src/3rdparty/google-ctemplate/src/ctemplate/template_string.h',
#'../src/3rdparty/google-ctemplate/src/diff_tpl_auto_escape.cc',
'../src/3rdparty/google-ctemplate/src/htmlparser/htmlparser.cc',
'../src/3rdparty/google-ctemplate/src/htmlparser/htmlparser_cpp.h',
'../src/3rdparty/google-ctemplate/src/htmlparser/htmlparser_fsm.h',
'../src/3rdparty/google-ctemplate/src/htmlparser/htmlparser.h',
'../src/3rdparty/google-ctemplate/src/htmlparser/jsparser.cc',
'../src/3rdparty/google-ctemplate/src/htmlparser/jsparser_fsm.h',
'../src/3rdparty/google-ctemplate/src/htmlparser/jsparser.h',
'../src/3rdparty/google-ctemplate/src/htmlparser/statemachine.cc',
'../src/3rdparty/google-ctemplate/src/htmlparser/statemachine.h',
'../src/3rdparty/google-ctemplate/src/indented_writer.h',
# '../src/3rdparty/google-ctemplate/src/make_tpl_varnames_h.cc',
'../src/3rdparty/google-ctemplate/src/per_expand_data.cc',
'../src/3rdparty/google-ctemplate/src/template_annotator.cc',
'../src/3rdparty/google-ctemplate/src/template_cache.cc',
'../src/3rdparty/google-ctemplate/src/template.cc',
'../src/3rdparty/google-ctemplate/src/template_dictionary.cc',
'../src/3rdparty/google-ctemplate/src/template_modifiers.cc',
'../src/3rdparty/google-ctemplate/src/template_modifiers_internal.h',
'../src/3rdparty/google-ctemplate/src/template_namelist.cc',
'../src/3rdparty/google-ctemplate/src/template_pathops.cc',
'../src/3rdparty/google-ctemplate/src/template_string.cc',
# '../src/3rdparty/google-ctemplate/src/tests/compile_test.cc',
# '../src/3rdparty/google-ctemplate/src/tests/htmlparser_test.cc',
# '../src/3rdparty/google-ctemplate/src/tests/statemachine_test_fsm.h',
# '../src/3rdparty/google-ctemplate/src/tests/template_cache_test.cc',
# '../src/3rdparty/google-ctemplate/src/tests/template_regtest.cc',
# '../src/3rdparty/google-ctemplate/src/tests/template_test_util.cc',
# '../src/3rdparty/google-ctemplate/src/tests/template_test_util.h',
# '../src/3rdparty/google-ctemplate/src/tests/template_test_util_test.cc',
      ],
     'direct_dependent_settings': {
#        'include_dirs': ['../src/3rdparty/google-ctemplate/src'],
      },
     'conditions': [
        ['OS == "linux"', {
          'sources!': [],
          'include_dirs': ['../src/3rdparty/google-ctemplate/src'],
          'direct_dependent_settings': {
            'include_dirs': ['../src/3rdparty/google-ctemplate/src'],
          },
          }],
        ['OS == "win"', {
          'sources': [
'../src/3rdparty/google-ctemplate/src/windows/config.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/per_expand_data.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/template_annotator.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/template_cache.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/template_dictionary.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/template_dictionary_interface.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/template_emitter.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/template_enums.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/template.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/template_modifiers.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/template_namelist.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/template_pathops.h',
'../src/3rdparty/google-ctemplate/src/windows/ctemplate/template_string.h',
'../src/3rdparty/google-ctemplate/src/windows/port.cc',
'../src/3rdparty/google-ctemplate/src/windows/port.h',
          ],
          'include_dirs': ['../src/3rdparty/google-ctemplate/src/windows', '../src/3rdparty/google-ctemplate/src'],
          'direct_dependent_settings': {
            'include_dirs': ['../src/3rdparty/google-ctemplate/src/windows'],
            'defines': ['CTEMPLATE_DLL_DECL='],
          },
          }]
      ],
    },
  ],
}