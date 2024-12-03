open(my $fh, '<', 'input.txt') or die "Could not open file 'input.txt' $!";

my @segments = split /(don't\(\)|do\(\))/,<$fh>;

my $result = '';
my $include = 1;

foreach my $segment (@segments) {
    if ($segment =~ /do\(\)/) {
        $include = 1;
        next
    } elsif ($segment =~ /don't\(\)/) {
        $include = 0;
        next
    }

    if ($include) {
        $result .= ($result ? '+' : '') . join('+', $segment =~ /mul\(\d+,\d+\)/g);
    }
}

print $result;
print eval $result; #107862689

sub mul { $_[0] * $_[1] }
