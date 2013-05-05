from wordstatistics import MRWordStatistics


def main():
    mr_job = MRWordStatistics(args=['--runner=local'])
    with mr_job.make_runner() as runner:
        runner.run()
        print 'Word' + '\t'.join(MRWordStatistics.WordDescription._fields)
        for line in runner.stream_output():
            word, aggregated_word_stats = mr_job.parse_output_line(line)
            print '{0}\t{1}\t{2}\t{3}'.format(word, *aggregated_word_stats)

if __name__ == '__main__':
    main()