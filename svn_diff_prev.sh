#!/bin/sh

echo "#!/bin/sh" > /tmp/cwdiff
echo "shift \$((\$# - 2))" >> /tmp/cwdiff
echo "wdiff -n \$1 \$2|colordiff" >>/tmp/cwdiff
chmod u+x /tmp/cwdiff

exec svn diff -rPREV --diff-cmd "/tmp/cwdiff" "$@"|less -R