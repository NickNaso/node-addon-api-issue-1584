{
  'target_defaults': {
     'include_dirs': [
          "<!(node -p \"require('node-api-headers').include_dir\")",
      ],
  },
  'targets': [
    {
      'target_name': 'addon',
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
      'cflags': [ '-fno-exceptions' ],
      'cflags_cc': [ '-fno-exceptions' ],
      'sources': [
        'addon.cc',
       ],
       'include_dirs': ["<!(node -p \"require('node-addon-api').include_dir\")" ],
       'conditions': [
        ['OS=="mac"', {
          'cflags+': ['-fvisibility=hidden'],
          'xcode_settings': {
            'OTHER_CFLAGS': ['-fvisibility=hidden'],
            'CLANG_CXX_LIBRARY': 'libc++',
            'CLANG_CXX_LIBRARY': 'libc++',
            'MACOSX_DEPLOYMENT_TARGET': '10.7',
            'GCC_ENABLE_CPP_EXCEPTIONS': 'NO',
          }
        }],
        ['OS=="win"', {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'ExceptionHandling': 0,
              'EnablePREfast': 'true',
            },
          },
        }],
      ],
    },
  ],
}
